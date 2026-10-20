import { CartProvider } from './context/CartContext';
import ProductList from './components/ProductList';
import Cart from './components/Cart';

function App() {
  return (
    <CartProvider>
      <div className="layout">
        <main>
          <h1>Mi Tienda React</h1>
          <ProductList />
        </main>
        <aside>
          <Cart />
        </aside>
      </div>
    </CartProvider>
  );
}

export default App;