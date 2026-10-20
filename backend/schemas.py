from pydantic import BaseModel


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: str
    stock: int

    model_config = {"from_attributes": True}


class CartItem(BaseModel):
    product_id: int
    quantity: int = 1


class CheckoutRequest(BaseModel):
    items: list[CartItem]
    email: str | None = None


class CheckoutResponse(BaseModel):
    order_id: str
    total: float
    status: str
    message: str