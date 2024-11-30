// src/App.js
import React, { useState, useEffect } from 'react';
import { Route, Routes, Navigate, useNavigate } from 'react-router-dom';
import './App.css';
import Product from './components/Product/Product';
import Header from './components/Header/Header';
import Login from './components/Login/Login';
import AdminProducts from './components/AdminProducts/AdminProducts';
import ProductForm from './components/AdminProducts/ProductForm';

function App() {
  const [products, setProducts] = useState([]);
  const [admin, setAdmin] = useState(null);
  const navigate = useNavigate();

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

  const handleLogin = (adminData) => {
    setAdmin(adminData);
    navigate('/admin/products');  // Redireciona após o login bem-sucedido
  };

  return (
    <div className="App">
      <Header />
      <main>
        <Routes>
          <Route path="/login" element={admin ? <Navigate to="/admin/products" /> : <Login onLogin={handleLogin} />} />
          <Route path="/" element={
            <section>
              <h2>Products</h2>
              <div className="products">
                {products.map(product => (
                  <Product key={product.productid} product={product} />
                ))}
              </div>
            </section>
          } />
          <Route path="/admin/products" element={admin ? <AdminProducts /> : <Navigate to="/login" />} />
          <Route path="/admin/products/new" element={admin ? <ProductForm /> : <Navigate to="/login" />} />
          <Route path="/admin/products/edit/:productid" element={admin ? <ProductForm /> : <Navigate to="/login" />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;