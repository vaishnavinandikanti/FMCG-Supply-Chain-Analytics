-- ==========================================
-- STEP 4: CREATE STAR SCHEMA TABLES
-- ==========================================

-- 1. Create DimProducts
SELECT DISTINCT
    product_name,
    category_name,
    department_name,
    order_item_product_price AS product_price
INTO DimProducts
FROM vw_supply_chain_clean;

-- 2. Create DimCustomers
SELECT DISTINCT
    customer_id,
    customer_fname,
    customer_lname,
    customer_segment,
    customer_city,
    customer_state,
    customer_country,
    market,
    order_region
INTO DimCustomers
FROM vw_supply_chain_clean;

-- 3. Create FactOrders
SELECT
    order_id,
    order_item_id,
    customer_id,
    product_name,  -- This acts as the link to DimProducts
    order_date,
    shipping_date,
    delivery_delay_days,
    shipping_mode,
    delivery_status,
    late_delivery_risk,
    order_item_quantity,
    sales,
    order_profit_per_order,
    order_item_discount,
    order_item_discount_rate
INTO FactOrders
FROM vw_supply_chain_clean;

-- 4. Create DimDate
SELECT DISTINCT
    CAST(order_date AS DATE) AS date_key,
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    DATENAME(MONTH, order_date) AS month_name,
    DAY(order_date) AS day,
    DATENAME(WEEKDAY, order_date) AS weekday
INTO DimDate
FROM vw_supply_chain_clean
WHERE order_date IS NOT NULL;