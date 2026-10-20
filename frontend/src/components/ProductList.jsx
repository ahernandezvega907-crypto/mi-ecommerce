import { useEffect, useState } from 'react';
import { useCart } from '../context/CartContext';

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const { addToCart } = useCart();

  useEffect(() => {
    fetch('https://mi-ecommerce-apibackend.onrender.com/products')
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Error cargando productos:", err));
  }, []);

  return (
    <div className="products-grid">
      {products.map((product) => (
        <div key={product.id} className="product-card">
          <img src={product.image} alt={product.name} />
          <h3>{product.name}</h3>
          <p>${product.price.toFixed(2)}</p>
          <button onClick={() => addToCart(product)}>Agregar al carrito</button>
        </div>
      ))}
    </div>
  );
}