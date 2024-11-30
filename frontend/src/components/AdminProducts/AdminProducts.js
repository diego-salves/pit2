// src/components/AdminProducts/AdminProducts.js
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './AdminProducts.css';

function AdminProducts() {
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

  const handleDelete = async (productid) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/products/${productid}`, {
        method: 'DELETE',
      });
      if (response.ok) {
        setProducts(products.filter(product => product.productid !== productid));
      } else {
        throw new Error('Failed to delete product');
      }
    } catch (error) {
      console.error('Failed to delete product:', error);
    }
  };

  return (
    <div className="admin-products">
      <h2>Manage Products</h2>
      <Link to="/admin/products/new" className="btn">Add New Product</Link>
      <div className="products">
        {products.map(product => (
          <div key={product.productid} className="product">
            <img src={product.image} alt={product.name} />
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <p>${product.price.toFixed(2)}</p>
            <div className="actions">
              <Link to={`/admin/products/edit/${product.productid}`} className="btn">Edit</Link>
              <button onClick={() => handleDelete(product.productid)} className="btn">Delete</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AdminProducts;
