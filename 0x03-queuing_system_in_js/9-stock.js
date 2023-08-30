const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Sample product data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, stock: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, stock: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, stock: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, stock: 5 }
];

// Create a Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// Express app
const app = express();
const port = 1245;

// Function to get item by ID
const getItemById = (id) => listProducts.find(product => product.itemId === id);

// Function to reserve stock in Redis
const reserveStockById = async (itemId) => {
  const item = getItemById(itemId);
  if (item) {
    await client.set(`item.${itemId}`, item.stock - 1);
  }
};

// Function to get current reserved stock from Redis
const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return parseInt(reservedStock) || 0;
};

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - currentReservedStock;

  res.json({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - currentReservedStock;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId);

  return res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

module.exports = app;
