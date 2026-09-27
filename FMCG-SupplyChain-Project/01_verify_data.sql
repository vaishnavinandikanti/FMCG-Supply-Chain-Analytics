-- ==========================================
-- STEP 1: VERIFY RAW DATA & CHECK QUALITY
-- ==========================================

-- 1. Verify the total row count (Expecting: 180,519)
SELECT COUNT(*) AS total_rows 
FROM raw_supply_chain;

-- 2. Check for nulls in critical columns
SELECT 
    SUM(CASE WHEN customer_lname IS NULL THEN 1 ELSE 0 END) AS null_customer_lname,
    SUM(CASE WHEN customer_zipcode IS NULL THEN 1 ELSE 0 END) AS null_customer_zipcode,
    SUM(CASE WHEN sales IS NULL THEN 1 ELSE 0 END) AS null_sales,
    SUM(CASE WHEN order_item_quantity IS NULL THEN 1 ELSE 0 END) AS null_quantity
FROM raw_supply_chain;

-- 3. Check for logical duplicates (Same Order ID and Order Item ID)
-- Expecting: Empty result set (No duplicates)
SELECT order_id, order_item_id, COUNT(*) as duplicate_count
FROM raw_supply_chain
GROUP BY order_id, order_item_id
HAVING COUNT(*) > 1;