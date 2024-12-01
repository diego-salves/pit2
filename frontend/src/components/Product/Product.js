import React from 'react';
import PropTypes from 'prop-types';
import './Product.css';
import cupcake from './cupcake.png';

function Product({ product }) {

  return (
    <div className="product">
      <img src={cupcake} alt={product.name} />
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
