// src/components/Product/Product.js
import React from 'react';
import PropTypes from 'prop-types';
import './Product.css';

function Product({ product }) {
  const imageUrl = 'https://example.com/default_image.jpg'; // URL de imagem padrão

  return (
    <div className="product">
      <img src={imageUrl} alt={product.name} />
      <h3>{product.name}</h3>
      <p>{product.description}</p>
      <p>${product.price.toFixed(2)}</p>
    </div>
  );
}

Product.propTypes = {
  product: PropTypes.shape({
    productid: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    stock: PropTypes.number.isRequired,
  }).isRequired,
};

export default Product;