import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show_product_detail():
    """Display the product detail page"""
    
    if st.session_state.selected_product is None:
        st.error("Please select a product first")
        if st.button("Go to Product Catalog", use_container_width=True):
            st.session_state.page = 'product_catalog'
            st.rerun()
        return
    
    product = st.session_state.selected_product
    
    # Premium product header with brand styling
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #1E3A8A 0%, #e63946 100%); 
         padding: 20px; border-radius: 10px; margin-bottom: 20px; color: white;">
        <h1 style="margin: 0; color: white;">{product['name']}</h1>
        <p style="margin: 5px 0 0 0; font-size: 0.9em;">Premium Denim Collection • Product ID: {product['id']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Layout with two columns
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # Replace default icon with better denim product images
        if "Denim" in product['name']:
            img_url = "https://images.unsplash.com/photo-1602293589930-45aad59ba3ab?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
        elif "Shirt" in product['name']:
            img_url = "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80" 
        elif "Jacket" in product['name']:
            img_url = "https://images.unsplash.com/photo-1551028719-00167b16eac5?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
        elif "T-Shirt" in product['name']:
            img_url = "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
        else:
            img_url = "https://images.unsplash.com/photo-1565084888279-aca607ecce0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
            
        # Display enhanced image with hover zoom effect
        st.markdown(f"""
        <div style="overflow: hidden; border-radius: 10px; margin: 10px 0;">
            <img src="{img_url}" width="100%" style="transition: transform 0.5s ease;"
                 onmouseover="this.style.transform='scale(1.05)';" 
                 onmouseout="this.style.transform='scale(1.0)';">
        </div>
        """, unsafe_allow_html=True)
        
        # Quick specs with premium styling
        st.markdown("""
        <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; margin: 15px 0;">
            <h3 style="color: #e63946; margin-top: 0;">Product Specifications</h3>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="margin: 10px 0;">
                <p style="margin: 0; font-weight: bold; color: #CCC;">Base Fabric</p>
                <p style="margin: 0; font-size: 1.1em;">{product['fabric']}</p>
            </div>
            <div style="margin: 10px 0;">
                <p style="margin: 0; font-weight: bold; color: #CCC;">Minimum Order Quantity</p>
                <p style="margin: 0; font-size: 1.1em;">{product['moq']} pieces</p>
            </div>
            <div style="margin: 10px 0;">
                <p style="margin: 0; font-weight: bold; color: #CCC;">Price Range</p>
                <p style="margin: 0; font-size: 1.1em;">{product['price_range']} per piece</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Additional product details with enhanced styling
        with st.expander("Product Description", expanded=True):
            st.markdown(f"""
            <div style="background-color: #2E2E2E; padding: 15px; border-radius: 10px;">
                <p style="line-height: 1.6;">{product['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Customization options
        st.subheader("Customize Your Order")
        
        # Fabric selection
        st.markdown("#### Fabric Options")
        fabric_options = ["Standard (as described)", "Premium Upgrade (+10%)", "Eco-Friendly Option (+15%)"]
        selected_fabric = st.selectbox("Select Fabric Type:", fabric_options)
        
        # Initialize variables to avoid LSP warnings
        selected_wash = None
        selected_color = None
        
        # Wash/Finish selection (if applicable)
        if 'wash_options' in product:
            st.markdown("#### Wash/Finish Options")
            selected_wash = st.selectbox("Select Wash/Finish:", product['wash_options'])
            # Store in session state
            st.session_state.current_selected_wash = selected_wash
        elif 'color_options' in product:
            st.markdown("#### Color Options")
            selected_color = st.selectbox("Select Base Color:", product['color_options'])
            # Store in session state
            st.session_state.current_selected_color = selected_color
        
        # Branding options
        st.markdown("#### Branding Options")
        branding_option = st.radio(
            "Select Branding Type:",
            ["Standard Woven Label", "Custom Branded Label (+$0.50/pc)", "No Branding (-$0.25/pc)"]
        )
        
        # Size & Quantity Grid
        st.markdown("#### Size Distribution")
        st.write("Enter quantity for each size (minimum total: " + str(product['moq']) + " pcs)")
        
        # Initialize variables to avoid LSP warnings
        size_quantities = {}
        total_quantity = product['moq']  # Default value
        
        # Create size distribution form
        if 'available_sizes' in product:
            sizes = product['available_sizes']
            
            # Create columns for size inputs
            size_cols = st.columns(len(sizes))
            
            # Create quantity input for each size
            for i, size in enumerate(sizes):
                with size_cols[i]:
                    size_quantities[size] = st.number_input(
                        size, 
                        min_value=0, 
                        value=int(product['moq'] / len(sizes)) if size in ['M', 'L', '34', '36'] else 0, 
                        step=10
                    )
            
            # Calculate total quantity
            total_quantity = sum(size_quantities.values())
            
            # Store in session state for access elsewhere
            st.session_state.current_size_quantities = size_quantities
            st.session_state.current_total_quantity = total_quantity
            
            # Show total with validation
            if total_quantity < product['moq']:
                st.warning(f"Total quantity ({total_quantity}) is below the minimum order quantity ({product['moq']}).")
            else:
                st.success(f"Total quantity: {total_quantity} pcs")
        
        # Special instructions
        st.markdown("#### Special Instructions")
        special_instructions = st.text_area("Add any special requirements or notes for this order:", height=100)
        
        # Action buttons section
        action_buttons = st.columns(2)
        
        with action_buttons[0]:
            # Add to cart button
            if st.button("Add to Order", use_container_width=True, type="primary"):
                # Create order item
                order_item = {
                    "product_id": product['id'],
                    "product_name": product['name'],
                    "fabric": selected_fabric,
                    "branding": branding_option,
                    "sizes": size_quantities if 'available_sizes' in product else {},
                    "total_quantity": total_quantity if 'available_sizes' in product else product['moq'],
                    "special_instructions": special_instructions,
                    "base_price": product['price_range']
                }
                
                # Add wash/color if applicable
                if 'wash_options' in product:
                    order_item["wash"] = selected_wash
                elif 'color_options' in product:
                    order_item["color"] = selected_color
                
                # Add to cart
                if 'cart' not in st.session_state:
                    st.session_state.cart = []
                
                st.session_state.cart.append(order_item)
                st.session_state.page = 'order_booking'
                st.rerun()
        
        with action_buttons[1]:
            # Market Price Intelligence button
            if st.button("🔍 Check Market Pricing", use_container_width=True):
                st.session_state.page = 'market_price_intelligence'
                st.rerun()
                
        # Add explanatory note for Market Price Intelligence
        st.info("💡 Use our Market Price Intelligence tool to analyze competitive pricing across the industry for similar products.")
    
    # Product details and specs section
    st.markdown("---")
    st.subheader("Detailed Specifications")
    
    tabs = st.tabs(["Materials & Construction", "Sizing Guide", "Production Timeline"])
    
    with tabs[0]:
        st.markdown("""
        ### Materials & Construction
        
        **Main Fabric:**
        - Type: """ + product['fabric'] + """
        - Composition: Varies based on selected option
        - Origin: Imported or locally sourced depending on availability
        
        **Construction Details:**
        - Industry standard stitching with reinforced seams
        - Double-needle construction for durability
        - Pre-shrunk fabric available on request
        """)
    
    with tabs[1]:
        # Sample size chart based on product type
        if any(x in product['id'] for x in ['T', 'TK']):  # Tops
            size_data = {
                "Size": ["S", "M", "L", "XL", "XXL"],
                "Chest (inches)": [38, 40, 42, 44, 46],
                "Length (inches)": [27, 28, 29, 30, 31],
                "Sleeve (inches)": [8, 8.5, 9, 9.5, 10]
            }
        else:  # Bottoms
            size_data = {
                "Size": ["30", "32", "34", "36", "38", "40"],
                "Waist (inches)": [30, 32, 34, 36, 38, 40],
                "Hip (inches)": [38, 40, 42, 44, 46, 48],
                "Inseam (inches)": [30, 31, 32, 33, 34, 34]
            }
        
        st.table(pd.DataFrame(size_data))
        
        st.markdown("""
        **Size Customization:**
        Custom sizing available for orders above 1000 pieces per size. Contact customer service for details.
        """)
    
    with tabs[2]:
        st.markdown("""
        ### Production & Delivery Timeline
        
        **Standard Production Timeline:**
        - Order confirmation: 2-3 business days
        - Sample approval: 7-10 business days
        - Production: 30-45 business days based on quantity
        - Quality check & packaging: 5-7 business days
        - Shipping: Depends on destination (typically 5-15 days)
        
        **Express Production:**
        Available for select products with a 20% rush fee. Reduces production time by 30%.
        """)
    
    # Related products with premium styling
    st.markdown("---")
    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2 style="color: #e63946; margin-top: 0;">Complete Your Collection</h2>
        <p style="color: #CCC; margin-bottom: 20px;">Customers who viewed this product also considered these items</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display related products in a row
    cols = st.columns(3)
    
    # Get product category and subcategory
    category = "Tops" if product['id'][0] == "T" else "Bottoms"
    subcategory = "Denims" if product['id'][1] == "D" else "Non-Denims" if product['id'][1] == "N" else "Knits"
    
    # Get related products (excluding current one)
    related_products = [p for p in get_related_products(category, subcategory) if p['id'] != product['id']][:3]
    
    for i, related in enumerate(related_products):
        with cols[i]:
            # Create premium card for related product
            st.markdown(f"""
            <div style="background-color: #2E2E2E; padding: 15px; border-radius: 10px; margin-bottom: 10px; 
                 box-shadow: 0 4px 8px rgba(0,0,0,0.2); transition: transform 0.3s ease, box-shadow 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-5px)';this.style.boxShadow='0 8px 16px rgba(0,0,0,0.3)';"
                 onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 8px rgba(0,0,0,0.2)';">
                <h3 style="color: #e63946; margin-bottom: 5px;">{related['name']}</h3>
                <p style="color: #ddd; margin: 0; font-size: 0.9em;">ID: {related['id']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Get appropriate image based on product name - using professional denim product images
            if "Denim Jeans" in related['name'] or "Slim Jeans" in related['name']:
                img_url = "https://images.unsplash.com/photo-1604176424472-9d997e67f540?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
            elif "Regular Jeans" in related['name'] or "Classic Jeans" in related['name']:
                img_url = "https://images.unsplash.com/photo-1542272604-787c3835535d?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80" 
            elif "Denim Shirt" in related['name']:
                img_url = "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80" 
            elif "Denim Jacket" in related['name']:
                img_url = "https://images.unsplash.com/photo-1591213954196-2d0ccb3f8d4c?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
            elif "T-Shirt" in related['name']:
                img_url = "https://images.unsplash.com/photo-1586363104862-3a5e2ab60d99?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
            elif "Shorts" in related['name']:
                img_url = "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
            else:
                img_url = "https://images.unsplash.com/photo-1565084888279-aca607ecce0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80"
            
            # Display image with rounded corners and hover zoom effect
            st.markdown(f"""
            <div style="overflow: hidden; border-radius: 10px; margin: 10px 0;">
                <img src="{img_url}" width="100%" style="transition: transform 0.5s ease;"
                     onmouseover="this.style.transform='scale(1.05)';" 
                     onmouseout="this.style.transform='scale(1.0)';">
            </div>
            """, unsafe_allow_html=True)
            
            # Quick specs display
            st.markdown(f"""
            <div style="margin: 10px 0;">
                <p style="margin: 0; font-weight: bold; color: #e63946;">{related['price_range']}</p>
                <p style="margin: 0; font-size: 0.9em; color: #CCC;">{related['fabric']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # View button with premium styling
            if st.button(f"🔍 View Details", key=f"related_{i}", use_container_width=True):
                st.session_state.selected_product = related
                st.rerun()

def get_related_products(category, subcategory):
    """Get related products based on category and subcategory"""
    # For simplicity, we're using the same function from product_catalog.py
    from product_catalog import get_product_types
    return get_product_types(category, subcategory)