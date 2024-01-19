import express from "express";
import dotenv from "dotenv";
import colors from 'colors';
import cors from "cors";
import connectDB from "./server/config/db.js";
import router from "./server/routes/authRoutes.js";

// Configure env
dotenv.config();

// Database config
connectDB();

// Express object
const app = express();
app.use(cors());
// Routes
app.use("/api/v1/auth", router);

// REST API
app.get("/", (req, res) => {
  res.send("<h1>Welcome to Trip adviser</h1>");
});

// PORT
const PORT = process.env.PORT || 8010;

// Run listen
app.listen(PORT, () => {
  console.log(
    `Server Running on ${process.env.DEV_MODE} mode on port ${PORT}`.bgCyan.white
  );
});
