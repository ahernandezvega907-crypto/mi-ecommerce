import { useCart } from '../context/CartContext';

export default function Cart() {
  const { cart, total, clearCart } = useCart();

  const handleCheckout = async () => {
    if (cart.length === 0) return alert('El carrito está vacío');
    
    const payload = {
      items: cart.map((item) => ({ product_id: item.id, quantity: item.quantity })),
      email: "cliente@test.com"
    };

    try {
      const res = await fetch('https://mi-ecommerce-apibackend.onrender.com/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      
      if (data.status === 'approved') {
        alert(`¡Pago exitoso! Orden: ${data.order_id} - Total: $${data.total}`);
        clearCart();
      } else {
        alert(`Pago rechazado: ${data.message}`);
      }
    } catch (error) {
      alert('Error de conexión con el servidor');
    }
  };

  return (
    <div className="cart-container">
      <h2>Tu Carrito</h2>
      {cart.length === 0 ? <p>Vacío</p> : (
        <ul>
          {cart.map((item) => (
            <li key={item.id}>
              {item.quantity} x {item.name} = ${(item.price * item.quantity).toFixed(2)}
            </li>
          ))}
        </ul>
      )}
      <h3>Total: ${total.toFixed(2)}</h3>
      <button className="pay-btn" onClick={handleCheckout}>Pagar</button>
    </div>
  );
}