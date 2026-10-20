# 🛒 E-commerce Full-Stack (React + FastAPI)

Una aplicación web de comercio electrónico completa, con listado de productos, carrito de compras y simulación de pagos.

## 🚀 Demo en vivo
- **Frontend:** [Ver tienda en Vercel](https://mi-ecommerce-chi.vercel.app)
- **Backend (API):** [Ver documentación en Render](https://mi-ecommerce-apibackend.onrender.com/docs)

## 🛠️ Tecnologías usadas
**Frontend:**
- React (con Vite)
- Context API (para el manejo del estado del carrito)
- CSS puro

**Backend:**
- Python 3.12
- FastAPI
- SQLAlchemy (ORM)
- SQLite (Base de datos)

## ✨ Características
- Listado de productos dinámico consumido desde la API.
- Carrito de compras con cálculo de totales en tiempo real.
- Simulación de pasarela de pago (aprobación/rechazo aleatorio).
- Descuento automático de stock en la base de datos tras una compra exitosa.

## ⚙️ Cómo correrlo localmente
*(Instrucciones breves por si otro desarrollador quiere clonarlo)*
1. Clonar el repo.
2. **Backend:** `cd backend`, activar entorno virtual, `pip install -r requirements.txt`, `uvicorn main:app --reload`.
3. **Frontend:** `cd frontend`, `npm install`, `npm run dev`.