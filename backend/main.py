from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, SessionLocal, engine


def seed():
    db = SessionLocal()
    try:
        if db.query(models.Product).count() == 0:
            db.add_all([
                models.Product(name="Camiseta Oversize", description="Algodón 100%", price=24.90, image="https://picsum.photos/seed/tee/400", stock=25),
                models.Product(name="Taza Cerámica", description="350 ml, apta microondas", price=12.50, image="https://picsum.photos/seed/mug/400", stock=40),
                models.Product(name="Auriculares BT", description="Bluetooth 5.3, 20h", price=59.99, image="https://picsum.photos/seed/head/400", stock=15),
                models.Product(name="Mochila Urbana", description="20L, antiagua", price=39.90, image="https://picsum.photos/seed/bag/400", stock=10),
                models.Product(name="Gorra Logo", description="Ajustable, unisex", price=18.00, image="https://picsum.photos/seed/cap/400", stock=30),
                models.Product(name="Termo Acero", description="500 ml, 12h caliente", price=22.00, image="https://picsum.photos/seed/termo/400", stock=20),
            ])
            db.commit()
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed()
    yield


app = FastAPI(title="Mi E-commerce API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"status": "ok", "mensaje": "API funcionando"}


@app.get("/products", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(models.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


@app.post("/checkout", response_model=schemas.CheckoutResponse)
def checkout(payload: schemas.CheckoutRequest, db: Session = Depends(get_db)):
    if not payload.items:
        raise HTTPException(status_code=400, detail="El carrito está vacío")

    total = 0.0
    for item in payload.items:
        product = db.get(models.Product, item.product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Producto {item.product_id} no existe")
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Cantidad inválida")
        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Sin stock suficiente de {product.name}")
        total += product.price * item.quantity
        product.stock -= item.quantity

    db.commit()

    # Simulación de pago: 90% aprueba, 10% rechaza
    approved = uuid4().int % 10 != 0
    status = "approved" if approved else "rejected"
    message = "Pago simulado aprobado" if approved else "Pago simulado rechazado (tarjeta ficticia)"

    return schemas.CheckoutResponse(
        order_id=str(uuid4())[:8].upper(),
        total=round(total, 2),
        status=status,
        message=message,
    )