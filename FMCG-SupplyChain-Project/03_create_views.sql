-- ==========================================
-- STEP 3: CREATE ANALYTICAL VIEW FOR REPORTING
-- ==========================================

-- Create a clean view that only exposes the columns needed for Excel/Tableau
CREATE OR ALTER VIEW vw_supply_chain_clean AS
SELECT 
    order_id,
    order_item_id,
    order_date_dateorders AS order_date,
    shipping_date_dateorders AS shipping_date,
    delivery_delay_days,
    shipping_mode,
    delivery_status,
    late_delivery_risk,
    customer_id,
    customer_fname,
    customer_lname,
    customer_segment,
    customer_city,
    customer_state,
    customer_country,
    market,
    order_region,
    order_status,
    category_name,
    department_name,
    product_name,
    order_item_quantity,
    sales,
    order_profit_per_order,
    order_item_product_price,
    order_item_discount,
    order_item_discount_rate
FROM raw_supply_chain;