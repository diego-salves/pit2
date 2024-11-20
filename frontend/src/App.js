import React, { useState, useEffect } from 'react';
import './App.css';
import Product from './components/Product/Product';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/products');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error('Failed to fetch products:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Cakemania!</h1>
        <p>Your favorite online cupcake store.</p>
      </header>
      <main>
        <section>
          <h2>Products</h2>
          <div className="products">
            {products.map(product => (
              <Product key={product.productid} product={product} />
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
