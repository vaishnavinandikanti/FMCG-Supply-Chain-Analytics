-- ==========================================
-- STEP 2: CLEAN MISSING VALUES & ADD METRICS
-- ==========================================

-- 1. Handle missing values (Impute with placeholders to preserve sales data)
UPDATE raw_supply_chain
SET customer_lname = 'Unknown'
WHERE customer_lname IS NULL;

UPDATE raw_supply_chain
SET customer_zipcode = 0
WHERE customer_zipcode IS NULL;
GO

-- 2. Add a new column for Delivery Delay safely
IF NOT EXISTS (SELECT * FROM sys.columns WHERE Name = N'delivery_delay_days' AND Object_ID = Object_ID(N'raw_supply_chain'))
BEGIN
    ALTER TABLE raw_supply_chain
    ADD delivery_delay_days INT;
END
GO

-- 3. Populate the new column
-- Logic: Positive = Late, Negative = Early, Zero = On Time
UPDATE raw_supply_chain
SET delivery_delay_days = days_for_shipping_real - days_for_shipment_scheduled;
GO

-- 4. Verify the cleaning worked
SELECT TOP 10 
    order_id, 
    customer_lname, 
    customer_zipcode, 
    days_for_shipping_real, 
    days_for_shipment_scheduled, 
    delivery_delay_days
FROM raw_supply_chain;