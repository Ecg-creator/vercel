import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

def show_market_price_intelligence():
    """Display the market price intelligence dashboard with pricing insights"""
    st.title("Market Price Intelligence")
    
    # Custom styling for the page
    st.markdown("""
    <style>
    .premium-header {
        background: linear-gradient(90deg, #e63946 0%, #1E3A8A 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .info-card {
        background-color: #212121;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 4px solid #e63946;
    }
    .metric-container {
        background-color: #2E2E2E;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .metric-title {
        font-size: 1.2em;
        color: #e63946;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 1.8em;
        font-weight: bold;
        color: white;
    }
    .metric-subtitle {
        font-size: 0.8em;
        color: #AAA;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Premium header for the tool
    st.markdown("""
    <div class="premium-header">
        <h1 style="margin: 0; font-size: 2.5em;">Market Price Intelligence</h1>
        <p style="margin: 5px 0 0 0;">Make data-driven pricing decisions with our proprietary analytics engine</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Disclaimer about legal compliance
    st.info("ℹ️ **Legal Compliance Notice:** This tool provides market averages and industry insights without direct competitor price listings, in accordance with antitrust regulations.")
    
    # Main content in tabs
    tabs = st.tabs(["Product Pricing Analysis", "Market Trends", "Regional Analytics", "Historical Data", "Margin Optimizer"])
    
    with tabs[0]:
        show_product_pricing_analysis()
    
    with tabs[1]:
        show_market_trends()
    
    with tabs[2]:
        show_regional_analytics()
    
    with tabs[3]:
        show_historical_data()
    
    with tabs[4]:
        show_margin_optimizer()

def show_product_pricing_analysis():
    """Show product pricing analysis section"""
    st.subheader("Product Pricing Analysis")
    
    # Product category selection
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        category = st.selectbox(
            "Product Category",
            options=["Denim Bottoms", "Denim Tops", "Non-Denim Bottoms", "Knit Products", "All Categories"]
        )
    
    with col2:
        sub_category = st.selectbox(
            "Sub-Category",
            options=["Jeans", "Shorts", "Jackets", "Shirts", "All Sub-Categories"]
        )
    
    with col3:
        price_range = st.select_slider(
            "Price Range",
            options=["Budget", "Mid-Range", "Premium", "Luxury", "All Ranges"]
        )
    
    # Create sample data
    price_data = {
        "Product": ["Slim Jeans", "Regular Jeans", "Classic Jeans", "Denim Shorts", "Cargo Shorts", 
                    "Denim Jacket", "Denim Shirt", "Chino Pants", "T-Shirts", "Polo Shirts"],
        "Category": ["Denim Bottoms", "Denim Bottoms", "Denim Bottoms", "Denim Bottoms", "Non-Denim Bottoms",
                   "Denim Tops", "Denim Tops", "Non-Denim Bottoms", "Knit Products", "Knit Products"],
        "Sub-Category": ["Jeans", "Jeans", "Jeans", "Shorts", "Shorts", 
                       "Jackets", "Shirts", "Pants", "T-Shirts", "Shirts"],
        "Min Price": [15.99, 14.50, 16.99, 10.99, 12.99, 
                     30.99, 22.99, 18.99, 7.99, 12.99],
        "Max Price": [25.99, 24.99, 28.99, 18.99, 19.99, 
                     44.99, 32.99, 29.99, 14.99, 22.99],
        "Avg Price": [20.99, 19.75, 22.99, 14.99, 16.99, 
                     37.99, 27.99, 24.99, 11.99, 17.99],
        "Market Volume": [35000, 42000, 28000, 18000, 15000, 
                         12000, 14000, 22000, 50000, 30000],
        "Price Trend": ["↑", "→", "↑", "↓", "→", 
                       "↑", "→", "↓", "→", "↑"],
        "Margin Potential": ["High", "Medium", "High", "Medium", "Low", 
                           "High", "Medium", "Low", "Medium", "High"],
    }
    
    df = pd.DataFrame(price_data)
    
    # Filter data based on selections
    filtered_df = df
    if category != "All Categories":
        filtered_df = filtered_df[filtered_df["Category"] == category]
    if sub_category != "All Sub-Categories":
        filtered_df = filtered_df[filtered_df["Sub-Category"] == sub_category]
    
    # Price range filtering (just for demonstration)
    if price_range == "Budget":
        filtered_df = filtered_df[filtered_df["Avg Price"] < 18]
    elif price_range == "Mid-Range":
        filtered_df = filtered_df[(filtered_df["Avg Price"] >= 18) & (filtered_df["Avg Price"] < 25)]
    elif price_range == "Premium":
        filtered_df = filtered_df[(filtered_df["Avg Price"] >= 25) & (filtered_df["Avg Price"] < 35)]
    elif price_range == "Luxury":
        filtered_df = filtered_df[filtered_df["Avg Price"] >= 35]
    
    # Display metrics row
    metrics_cols = st.columns(4)
    
    with metrics_cols[0]:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-title">Average Market Price</div>
            <div class="metric-value">$%.2f</div>
            <div class="metric-subtitle">Across selected categories</div>
        </div>
        """ % filtered_df["Avg Price"].mean(), unsafe_allow_html=True)
    
    with metrics_cols[1]:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-title">Price Range</div>
            <div class="metric-value">$%.2f - $%.2f</div>
            <div class="metric-subtitle">Min - Max in market</div>
        </div>
        """ % (filtered_df["Min Price"].min(), filtered_df["Max Price"].max()), unsafe_allow_html=True)
    
    with metrics_cols[2]:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-title">Total Market Volume</div>
            <div class="metric-value">%s</div>
            <div class="metric-subtitle">Units per season</div>
        </div>
        """ % f"{filtered_df['Market Volume'].sum():,}", unsafe_allow_html=True)
    
    with metrics_cols[3]:
        trend_counts = [
            filtered_df["Price Trend"].value_counts().get("↑", 0),
            filtered_df["Price Trend"].value_counts().get("→", 0),
            filtered_df["Price Trend"].value_counts().get("↓", 0)
        ]
        if max(trend_counts) == trend_counts[0]:
            market_trend = "Rising"
            trend_color = "#4CAF50"
        elif max(trend_counts) == trend_counts[1]:
            market_trend = "Stable"
            trend_color = "#2196F3"
        else:
            market_trend = "Declining"
            trend_color = "#F44336"
        
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-title">Market Trend</div>
            <div class="metric-value" style="color: {trend_color}">{market_trend}</div>
            <div class="metric-subtitle">Current 60-day outlook</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Price range visualization
    st.subheader("Market Price Ranges")
    
    # Create a cleaner visualization of price ranges
    fig = go.Figure()
    
    for i, row in filtered_df.iterrows():
        fig.add_trace(go.Bar(
            x=[row["Product"]],
            y=[row["Max Price"] - row["Min Price"]],
            base=[row["Min Price"]],
            marker_color='#1E3A8A',
            name=row["Product"],
            customdata=np.array([[row["Avg Price"], row["Market Volume"], row["Margin Potential"]]]),
            hovertemplate="<b>%{x}</b><br>" +
                          "Price Range: $%{base:.2f} - $%{y:.2f}<br>" +
                          "Average Price: $%{customdata[0]:.2f}<br>" +
                          "Market Volume: %{customdata[1]:,} units<br>" +
                          "Margin Potential: %{customdata[2]}<extra></extra>"
        ))
    
    # Add markers for average price
    for i, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(
            x=[row["Product"]],
            y=[row["Avg Price"]],
            mode='markers',
            marker=dict(color='#e63946', size=10, symbol='diamond'),
            name=row["Product"] + " Avg",
            showlegend=False,
            hoverinfo='skip'
        ))
    
    fig.update_layout(
        title="Market Price Ranges by Product",
        xaxis_title="",
        yaxis_title="Price ($)",
        barmode='overlay',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=40, b=80),
        hovermode="closest",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        font=dict(
            color="white"
        ),
        xaxis=dict(
            tickangle=-45
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed market price analysis table
    st.subheader("Detailed Market Analysis")
    st.write("Analysis of current market pricing across various product categories and competitors")
    
    st.dataframe(
        filtered_df[["Product", "Category", "Sub-Category", "Min Price", "Avg Price", "Max Price", "Price Trend", "Margin Potential"]],
        hide_index=True,
        use_container_width=True
    )
    
    # Price positioning recommendation
    margin_score = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }
    
    # Prevent division by zero if filtered_df is empty
    if len(filtered_df) > 0:
        avg_margin_potential = sum([margin_score.get(mp, 0) for mp in filtered_df["Margin Potential"]]) / len(filtered_df)
    else:
        avg_margin_potential = 2.0  # Default to medium if no data is available
    
    st.markdown("### 🧠 Price Positioning Recommendation")
    
    recommendation_cols = st.columns([3, 1])
    
    with recommendation_cols[0]:
        if avg_margin_potential > 2.5:
            st.success("The selected product category shows strong margin potential with limited price sensitivity. Consider a premium pricing strategy 10-15% above market average to maximize profitability while maintaining competitive positioning.")
        elif avg_margin_potential > 1.5:
            st.info("This product category shows moderate price elasticity. We recommend pricing within 5% of market average with selective premium options to optimize volume while maintaining healthy margins.")
        else:
            st.warning("This category is highly price-sensitive with significant competition. Consider a competitive pricing strategy 5-10% below market average to drive volume, with cost optimization to maintain profitability.")
    
    with recommendation_cols[1]:
        if avg_margin_potential > 2.5:
            recommendation = "Premium ✓"
            score = 90
            color = "#4CAF50"
        elif avg_margin_potential > 1.5:
            recommendation = "Balanced ✓"
            score = 75
            color = "#2196F3"
        else:
            recommendation = "Competitive ✓"
            score = 60
            color = "#E65100"
            
        st.markdown(f"""
        <div class="metric-container" style="height: 160px;">
            <div class="metric-title">Recommended Strategy</div>
            <div class="metric-value" style="color: {color}; font-size: 1.4em">{recommendation}</div>
            <div style="font-size: 2.5em; color: {color}; margin: 5px 0;">{score}%</div>
            <div class="metric-subtitle">Confidence score</div>
        </div>
        """, unsafe_allow_html=True)

def show_market_trends():
    """Show market trends section"""
    st.subheader("Market Pricing Trends")
    
    # Mock data for the past 24 months
    months = 24
    today = datetime.now()
    dates = [(today - timedelta(days=30*i)).strftime("%b %Y") for i in range(months)]
    dates.reverse()  # Start from oldest
    
    # Trend data for different product types
    np.random.seed(42)  # For reproducible results
    
    # Generate some realistic trend data with seasonal patterns
    base_price = 20
    seasonal_pattern = np.sin(np.linspace(0, 2*np.pi, 12))  # 12-month seasonal pattern
    
    # Extend seasonal pattern to 24 months
    seasonal_pattern = np.tile(seasonal_pattern, 2)
    
    # Add trend and noise for different product categories
    denim_data = base_price + np.linspace(0, 3, months) + seasonal_pattern * 1.5 + np.random.normal(0, 0.5, months)
    non_denim_data = base_price - 2 + np.linspace(0, 1, months) + seasonal_pattern * 1.2 + np.random.normal(0, 0.3, months)
    knit_data = base_price - 5 + np.linspace(0, 2, months) + seasonal_pattern * 0.8 + np.random.normal(0, 0.4, months)
    premium_data = base_price + 10 + np.linspace(0, 4, months) + seasonal_pattern * 2 + np.random.normal(0, 0.7, months)
    
    # Create the trend dataframe
    trend_data = pd.DataFrame({
        "Month": dates,
        "Denim Products": denim_data,
        "Non-Denim Products": non_denim_data,
        "Knit Products": knit_data,
        "Premium Collections": premium_data
    })
    
    # Trend filters
    filter_cols = st.columns([1, 1, 1])
    
    with filter_cols[0]:
        trend_period = st.radio(
            "Time Period",
            options=["Last 6 Months", "Last 12 Months", "Last 24 Months"],
            horizontal=True
        )
    
    with filter_cols[1]:
        categories_to_show = st.multiselect(
            "Product Categories",
            options=["Denim Products", "Non-Denim Products", "Knit Products", "Premium Collections"],
            default=["Denim Products", "Non-Denim Products", "Knit Products"]
        )
    
    with filter_cols[2]:
        chart_type = st.radio(
            "Chart Type",
            options=["Line", "Area"],
            horizontal=True
        )
    
    # Filter data based on selected period
    if trend_period == "Last 6 Months":
        filtered_trend_data = trend_data.iloc[-6:]
    elif trend_period == "Last 12 Months":
        filtered_trend_data = trend_data.iloc[-12:]
    else:
        filtered_trend_data = trend_data
    
    # Create the trend chart
    if chart_type == "Line":
        fig = px.line(
            filtered_trend_data, 
            x="Month", 
            y=categories_to_show,
            labels={"value": "Average Price ($)", "variable": "Product Category"},
            title=f"Average Market Pricing Trends - {trend_period}",
            color_discrete_map={
                "Denim Products": "#1E3A8A", 
                "Non-Denim Products": "#43A047", 
                "Knit Products": "#E65100",
                "Premium Collections": "#e63946"
            }
        )
    else:  # Area chart
        fig = px.area(
            filtered_trend_data, 
            x="Month", 
            y=categories_to_show,
            labels={"value": "Average Price ($)", "variable": "Product Category"},
            title=f"Average Market Pricing Trends - {trend_period}",
            color_discrete_map={
                "Denim Products": "#1E3A8A", 
                "Non-Denim Products": "#43A047", 
                "Knit Products": "#E65100",
                "Premium Collections": "#e63946"
            }
        )
    
    fig.update_layout(
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=60, b=40),
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        font=dict(
            color="white"
        )
    )
    
    # Add annotations for market events
    market_events = [
        {"date": dates[-6], "event": "Cotton Price Spike", "impact": "↑", "color": "#F44336"},
        {"date": dates[-3], "event": "New Tariff Implementation", "impact": "↑", "color": "#F44336"},
        {"date": dates[-10], "event": "New Competitor Entry", "impact": "↓", "color": "#4CAF50"},
    ]
    
    for event in market_events:
        if event["date"] in filtered_trend_data["Month"].values:
            # Find the maximum y value for the event date
            event_date_index = filtered_trend_data[filtered_trend_data["Month"] == event["date"]].index[0]
            event_y_values = [filtered_trend_data[cat].iloc[event_date_index] for cat in categories_to_show if cat in filtered_trend_data.columns]
            
            if event_y_values:
                max_y = max(event_y_values) + 1  # Add some padding
                
                fig.add_annotation(
                    x=event["date"],
                    y=max_y,
                    text=f"{event['impact']} {event['event']}",
                    showarrow=True,
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor=event["color"],
                    font=dict(color="white", size=10),
                    bgcolor=event["color"],
                    bordercolor=event["color"],
                    borderwidth=1,
                    borderpad=4,
                    opacity=0.8
                )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Market insights for price trends
    st.markdown("### Key Market Insights")
    
    insight_cols = st.columns(2)
    
    with insight_cols[0]:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">Seasonal Pricing Patterns</h4>
            <p>Denim product prices typically peak during Q1 (January-March) and Q3 (July-September), aligning with new seasonal collections. Consider timing product launches to coincide with these periods of higher market pricing.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">Raw Material Impact</h4>
            <p>Cotton price fluctuations continue to show a 2-3 month delayed impact on final product pricing. Current cotton futures suggest a 5-8% increase in base material costs over the next quarter.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_cols[1]:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">Competitive Dynamics</h4>
            <p>The premium denim segment has shown increased price resilience, with consumers prioritizing quality and sustainability over price. This creates opportunity for margin expansion in high-quality denim products.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">Emerging Trends</h4>
            <p>Sustainable and eco-friendly denim commands a 15-20% price premium, with growing consumer willingness to pay for environmentally responsible manufacturing processes.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Price elasticity analysis
    st.subheader("Price Elasticity Analysis")
    st.write("Understanding how sales volume responds to price changes across categories")
    
    # Sample elasticity data
    elasticity_data = {
        "Category": ["Denim Jeans", "Denim Shirts", "Denim Jackets", "T-Shirts", "Chinos", "Cargo Pants"],
        "Price Elasticity": [-1.3, -0.9, -0.7, -2.1, -1.5, -1.8],
        "Price Range": ["$15-25", "$20-30", "$30-45", "$8-15", "$18-28", "$20-30"],
        "Volume Impact": ["High", "Medium", "Low", "Very High", "High", "High"]
    }
    
    elasticity_df = pd.DataFrame(elasticity_data)
    
    # Create elasticity visualization
    fig = px.bar(
        elasticity_df,
        x="Category",
        y="Price Elasticity",
        color="Volume Impact",
        color_discrete_map={
            "Very High": "#F44336",
            "High": "#FF9800",
            "Medium": "#2196F3",
            "Low": "#4CAF50"
        },
        title="Price Elasticity by Product Category",
        labels={"Price Elasticity": "Price Elasticity Coefficient", "Category": ""},
        hover_data=["Price Range"]
    )
    
    fig.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=60, b=40),
        font=dict(
            color="white"
        )
    )
    
    # Add a reference line at -1 (unit elasticity)
    fig.add_shape(
        type="line",
        x0=-0.5,
        y0=-1,
        x1=len(elasticity_df)-0.5,
        y1=-1,
        line=dict(
            color="#FFFFFF",
            width=1,
            dash="dash",
        )
    )
    
    # Add annotation explaining the reference line
    fig.add_annotation(
        x=len(elasticity_df)-1,
        y=-1.05,
        text="Unit Elasticity",
        showarrow=False,
        font=dict(
            color="#FFFFFF",
            size=10
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Explanation of price elasticity
    st.info("""
    **Understanding Price Elasticity:**
    - Price elasticity measures how sensitive sales volume is to price changes
    - Values below -1 (more negative) indicate higher price sensitivity
    - Values between -1 and 0 indicate lower price sensitivity
    - More elastic products (below -1) should be priced competitively
    - Less elastic products (above -1) have more pricing flexibility
    """)

def show_regional_analytics():
    """Show regional analytics section"""
    st.subheader("Regional Price Analysis")
    
    # Regional filters
    filter_cols = st.columns([1, 1, 1, 1])
    
    with filter_cols[0]:
        product_type = st.selectbox(
            "Product Type",
            options=["Denim Jeans", "Denim Shirts", "Denim Jackets", "All Denim Products"]
        )
    
    with filter_cols[1]:
        price_segment = st.selectbox(
            "Price Segment",
            options=["Budget", "Mid-Range", "Premium", "All Segments"]
        )
    
    with filter_cols[2]:
        time_period = st.selectbox(
            "Time Period",
            options=["Current Quarter", "Previous Quarter", "Year to Date", "Last Year"]
        )
    
    with filter_cols[3]:
        view_type = st.selectbox(
            "View",
            options=["Map View", "Comparison View"]
        )
    
    # Regional pricing data
    regional_data = {
        "Region": ["North India", "South India", "East India", "West India", "Central India", "Northeast India"],
        "Average Price": [19.99, 21.99, 18.50, 22.99, 20.50, 19.75],
        "Price Growth": [2.5, 3.8, 1.2, 4.5, 2.8, 1.5],
        "Volume Growth": [5.2, 3.5, 2.8, 6.5, 4.2, 2.0],
        "Price Sensitivity": [3.2, 2.8, 3.5, 2.5, 3.0, 3.4],
        "Market Share": [25, 22, 15, 28, 8, 2]
    }
    
    regional_df = pd.DataFrame(regional_data)
    
    if view_type == "Map View":
        # Display a mock map for now (in a real app, this would be a proper map)
        st.image("https://www.researchgate.net/profile/Zaffar-Sulaiman/publication/344466197/figure/fig1/AS:941951151484928@1601544385391/Map-of-India-showing-the-six-regions-of-India-North-East-West-Central-and-South.jpg", 
                 caption="Regions of India with pricing heat map",
                 use_column_width=True)
        
        # Regional metrics below the map
        metric_cols = st.columns(len(regional_df))
        
        for i, (_, row) in enumerate(regional_df.iterrows()):
            with metric_cols[i]:
                # Determine price trend color
                if row["Price Growth"] > 3.0:
                    price_color = "#F44336"  # Red for high growth
                elif row["Price Growth"] > 2.0:
                    price_color = "#FF9800"  # Orange for medium growth
                else:
                    price_color = "#4CAF50"  # Green for low growth
                
                st.markdown(f"""
                <div class="metric-container" style="height: 160px;">
                    <div class="metric-title">{row["Region"]}</div>
                    <div class="metric-value">${row["Average Price"]:.2f}</div>
                    <div style="font-size: 1.0em; color: {price_color}; margin: 5px 0;">+{row["Price Growth"]}%</div>
                    <div class="metric-subtitle">Market Share: {row["Market Share"]}%</div>
                </div>
                """, unsafe_allow_html=True)
    else:  # Comparison View
        # Create a comprehensive comparison view
        fig = px.scatter(
            regional_df,
            x="Price Sensitivity",
            y="Average Price",
            size="Market Share",
            color="Price Growth",
            hover_name="Region",
            color_continuous_scale=px.colors.diverging.RdBu_r,
            color_continuous_midpoint=2.5,
            title="Regional Price Analysis Matrix",
            labels={
                "Price Sensitivity": "Price Sensitivity Index (Lower = Less Sensitive)",
                "Average Price": "Average Price ($)",
                "Market Share": "Market Share (%)",
                "Price Growth": "Price Growth (%)"
            },
            size_max=40
        )
        
        # Add annotations for each region
        for i, row in regional_df.iterrows():
            fig.add_annotation(
                x=row["Price Sensitivity"],
                y=row["Average Price"],
                text=row["Region"],
                showarrow=False,
                font=dict(
                    color="white",
                    size=10
                ),
                bgcolor="rgba(0,0,0,0.5)",
                bordercolor="white",
                borderwidth=1,
                borderpad=4,
                opacity=0.8
            )
        
        fig.update_layout(
            height=600,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=60, b=40),
            font=dict(
                color="white"
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Regional pricing strategies
    st.subheader("Regional Pricing Strategy Recommendations")
    
    # Display regional pricing recommendations in a table
    strategy_data = {
        "Region": ["North India", "South India", "East India", "West India", "Central India", "Northeast India"],
        "Pricing Strategy": ["Balanced", "Premium", "Competitive", "Premium+", "Balanced", "Value-focused"],
        "Optimal Price Point": ["$20.50", "$23.99", "$17.99", "$24.50", "$20.99", "$18.99"],
        "Projected Margin": ["32%", "36%", "28%", "38%", "33%", "30%"],
        "Volume Impact": ["Neutral", "Slight decrease", "Moderate increase", "Slight decrease", "Neutral", "Moderate increase"],
        "Recommendation": [
            "Maintain current pricing with selective premium options", 
            "Increase prices 5-8% focusing on quality perception", 
            "Reduce prices 2-3% with volume-based incentives",
            "Premium positioning with enhanced feature set",
            "Targeted discounting during festival seasons only",
            "Focus on value bundles with multi-purchase incentives"
        ]
    }
    
    strategy_df = pd.DataFrame(strategy_data)
    
    # Apply color coding to the strategy df
    def highlight_strategy(val):
        if val == "Premium+" or val == "Premium":
            return 'background-color: rgba(230, 57, 70, 0.2); color: #e63946; font-weight: bold'
        elif val == "Balanced":
            return 'background-color: rgba(30, 58, 138, 0.2); color: #1E3A8A; font-weight: bold'
        elif val == "Competitive" or val == "Value-focused":
            return 'background-color: rgba(67, 160, 71, 0.2); color: #43A047; font-weight: bold'
        else:
            return ''
    
    # Apply highlighting to the strategy column
    styled_df = strategy_df.style.applymap(highlight_strategy, subset=['Pricing Strategy'])
    
    # Display the table with scrolling
    st.dataframe(styled_df, use_container_width=True, height=250)
    
    # Regional insights
    st.markdown("### Regional Market Insights")
    
    insight_cols = st.columns(2)
    
    with insight_cols[0]:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">West India Premium Market</h4>
            <p>The West India market continues to show the highest premium pricing tolerance, with Mumbai and Pune leading in consumer willingness to pay for premium denim products. Focus on exclusive designs and premium detailing for this region.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">East India Value Preference</h4>
            <p>East India shows the highest price sensitivity. Focus on entry-level premium products with essential features and competitive pricing. Bundle offers show particularly strong performance in this region.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with insight_cols[1]:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">South India Quality Focus</h4>
            <p>South Indian consumers prioritize quality and durability over price, with Bangalore and Chennai showing strong preference for premium sustainable products. Emphasize quality messaging in marketing materials.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #e63946; margin-top: 0;">North India Seasonal Variation</h4>
            <p>North India shows the highest seasonal price fluctuation, with winter products commanding up to 25% premium. Implement dynamic seasonal pricing strategies for this region to maximize revenue.</p>
        </div>
        """, unsafe_allow_html=True)

def show_historical_data():
    """Show historical data analysis section"""
    st.subheader("Historical Pricing Analytics")
    
    # Time period selection
    time_cols = st.columns([2, 1])
    
    with time_cols[0]:
        date_range = st.date_input(
            "Select Date Range",
            value=(datetime.now() - timedelta(days=365), datetime.now()),
            max_value=datetime.now()
        )
    
    with time_cols[1]:
        aggregation = st.radio(
            "Aggregation",
            options=["Monthly", "Quarterly", "Yearly"],
            horizontal=True
        )
    
    # Generate historical price data
    np.random.seed(42)
    
    # Create a date range
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        # Default to 1 year of data
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
    
    # Generate dates
    days = (end_date - start_date).days + 1
    dates = [start_date + timedelta(days=i) for i in range(days)]
    
    # Generate price data
    base_price = 20
    trend = np.linspace(0, 3, len(dates))  # Upward trend
    
    # Add seasonal component (yearly cycle)
    seasonal = 2 * np.sin(np.linspace(0, 2*np.pi * (days/365), len(dates)))
    
    # Add weekly pattern
    weekly = 0.5 * np.sin(np.linspace(0, 2*np.pi * (days/7), len(dates)))
    
    # Add noise
    noise = np.random.normal(0, 0.5, len(dates))
    
    # Combine components
    prices = base_price + trend + seasonal + weekly + noise
    
    # Create DataFrame
    hist_data = pd.DataFrame({
        "Date": dates,
        "Price": prices,
        "Year": [d.year for d in dates],
        "Month": [d.month for d in dates],
        "Quarter": [f"Q{(d.month-1)//3+1}" for d in dates]
    })
    
    # Aggregate based on selection
    if aggregation == "Monthly":
        grouped = hist_data.groupby([hist_data["Year"], hist_data["Month"]]).agg({
            "Price": ["mean", "min", "max", "std"]
        }).reset_index()
        grouped["Period"] = grouped.apply(lambda x: f"{x['Year']}-{x['Month']:02d}", axis=1)
    elif aggregation == "Quarterly":
        grouped = hist_data.groupby([hist_data["Year"], hist_data["Quarter"]]).agg({
            "Price": ["mean", "min", "max", "std"]
        }).reset_index()
        grouped["Period"] = grouped.apply(lambda x: f"{x['Year']} {x['Quarter']}", axis=1)
    else:  # Yearly
        grouped = hist_data.groupby(hist_data["Year"]).agg({
            "Price": ["mean", "min", "max", "std"]
        }).reset_index()
        grouped["Period"] = grouped["Year"].astype(str)
    
    # Rename columns for better display
    grouped.columns = ['_'.join(col).strip('_') for col in grouped.columns.values]
    grouped.rename(columns={
        "Price_mean": "Average Price",
        "Price_min": "Minimum Price",
        "Price_max": "Maximum Price",
        "Price_std": "Price Std Dev"
    }, inplace=True)
    
    # Create historical price chart
    fig = go.Figure()
    
    # Add range area (min to max)
    fig.add_trace(go.Scatter(
        x=grouped["Period"],
        y=grouped["Maximum Price"],
        mode='lines',
        line=dict(width=0),
        name="Price Range",
        showlegend=False
    ))
    
    fig.add_trace(go.Scatter(
        x=grouped["Period"],
        y=grouped["Minimum Price"],
        mode='lines',
        line=dict(width=0),
        fill='tonexty',
        fillcolor='rgba(30, 58, 138, 0.2)',
        name="Price Range",
    ))
    
    # Add average price line
    fig.add_trace(go.Scatter(
        x=grouped["Period"],
        y=grouped["Average Price"],
        mode='lines+markers',
        line=dict(color='#e63946', width=3),
        marker=dict(size=8),
        name="Average Price"
    ))
    
    fig.update_layout(
        title=f"Historical Price Trends ({aggregation} Aggregation)",
        xaxis_title="",
        yaxis_title="Price ($)",
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=60, b=80),
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        font=dict(
            color="white"
        ),
        xaxis=dict(
            tickangle=-45
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Price volatility analysis
    st.subheader("Price Volatility Analysis")
    
    # Calculate rolling volatility (standard deviation)
    if len(hist_data) > 30:  # Need enough data points
        hist_data["30D_Rolling_Std"] = hist_data["Price"].rolling(window=30).std()
        
        # Create volatility chart
        fig = px.line(
            hist_data.dropna(),  # Remove NaN values from rolling window
            x="Date",
            y="30D_Rolling_Std",
            title="30-Day Rolling Price Volatility",
            labels={"30D_Rolling_Std": "Price Volatility (Std Dev)", "Date": ""}
        )
        
        fig.update_traces(line_color="#e63946")
        
        fig.update_layout(
            height=350,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=60, b=40),
            font=dict(
                color="white"
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Year-over-year comparison
    st.subheader("Year-over-Year Comparison")
    
    # Prepare data for YoY comparison
    hist_data["MonthDay"] = hist_data["Date"].apply(lambda x: x.strftime("%m-%d"))
    
    # Get unique years
    years = sorted(hist_data["Year"].unique())
    
    if len(years) > 1:
        # Create YoY comparison
        fig = go.Figure()
        
        for year in years:
            year_data = hist_data[hist_data["Year"] == year]
            
            fig.add_trace(go.Scatter(
                x=year_data["MonthDay"],
                y=year_data["Price"],
                mode='lines',
                name=str(year)
            ))
        
        fig.update_layout(
            title="Year-over-Year Price Comparison",
            xaxis_title="Month-Day",
            yaxis_title="Price ($)",
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=60, b=40),
            hovermode="x unified",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            font=dict(
                color="white"
            )
        )
        
        # Add month markers
        month_markers = [
            {"date": "01-01", "label": "Jan"},
            {"date": "02-01", "label": "Feb"},
            {"date": "03-01", "label": "Mar"},
            {"date": "04-01", "label": "Apr"},
            {"date": "05-01", "label": "May"},
            {"date": "06-01", "label": "Jun"},
            {"date": "07-01", "label": "Jul"},
            {"date": "08-01", "label": "Aug"},
            {"date": "09-01", "label": "Sep"},
            {"date": "10-01", "label": "Oct"},
            {"date": "11-01", "label": "Nov"},
            {"date": "12-01", "label": "Dec"}
        ]
        
        for marker in month_markers:
            fig.add_vline(
                x=marker["date"],
                line_width=1,
                line_dash="dash",
                line_color="rgba(255, 255, 255, 0.2)"
            )
            
            # Add month label
            fig.add_annotation(
                x=marker["date"],
                y=hist_data["Price"].min(),
                text=marker["label"],
                showarrow=False,
                yshift=-20,
                font=dict(size=10, color="rgba(255, 255, 255, 0.7)")
            )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Historical data table with filters
    st.subheader("Historical Data Analysis")
    
    # Add filter expander
    with st.expander("Advanced Filters and Analysis Options"):
        filter_cols = st.columns(3)
        
        with filter_cols[0]:
            price_filter = st.slider(
                "Price Range",
                min_value=float(hist_data["Price"].min()),
                max_value=float(hist_data["Price"].max()),
                value=(float(hist_data["Price"].min()), float(hist_data["Price"].max()))
            )
        
        with filter_cols[1]:
            if aggregation == "Monthly":
                month_filter = st.multiselect(
                    "Months",
                    options=sorted(hist_data["Month"].unique()),
                    default=sorted(hist_data["Month"].unique())
                )
            elif aggregation == "Quarterly":
                quarter_filter = st.multiselect(
                    "Quarters",
                    options=sorted(hist_data["Quarter"].unique()),
                    default=sorted(hist_data["Quarter"].unique())
                )
        
        with filter_cols[2]:
            year_filter = st.multiselect(
                "Years",
                options=sorted(hist_data["Year"].unique()),
                default=sorted(hist_data["Year"].unique())
            )
    
    # Apply filters
    filtered_data = hist_data[
        (hist_data["Price"] >= price_filter[0]) &
        (hist_data["Price"] <= price_filter[1]) &
        (hist_data["Year"].isin(year_filter))
    ]
    
    if aggregation == "Monthly" and 'month_filter' in locals():
        filtered_data = filtered_data[filtered_data["Month"].isin(month_filter)]
    elif aggregation == "Quarterly" and 'quarter_filter' in locals():
        filtered_data = filtered_data[filtered_data["Quarter"].isin(quarter_filter)]
    
    # Display statistics on filtered data
    stat_cols = st.columns(4)
    
    with stat_cols[0]:
        st.metric("Average Price", f"${filtered_data['Price'].mean():.2f}")
    
    with stat_cols[1]:
        st.metric("Price Range", f"${filtered_data['Price'].min():.2f} - ${filtered_data['Price'].max():.2f}")
    
    with stat_cols[2]:
        st.metric("Standard Deviation", f"${filtered_data['Price'].std():.2f}")
    
    with stat_cols[3]:
        # Calculate price trend (last value - first value) / first value
        if len(filtered_data) > 1:
            first_price = filtered_data.iloc[0]["Price"]
            last_price = filtered_data.iloc[-1]["Price"]
            price_change = ((last_price - first_price) / first_price) * 100
            st.metric("Overall Trend", f"{price_change:.1f}%", delta=f"{price_change:.1f}%")
        else:
            st.metric("Overall Trend", "N/A")
    
    # Show a sample of the filtered data
    st.dataframe(
        filtered_data[["Date", "Price", "Year", "Month", "Quarter"]].sort_values("Date", ascending=False).head(100),
        use_container_width=True
    )
    
    # Download option
    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')
    
    csv = convert_df_to_csv(filtered_data[["Date", "Price", "Year", "Month", "Quarter"]])
    
    st.download_button(
        label="📥 Download Historical Data",
        data=csv,
        file_name=f'price_history_{datetime.now().strftime("%Y%m%d")}.csv',
        mime='text/csv',
    )

def show_margin_optimizer():
    """Show margin optimizer section"""
    st.subheader("Margin Optimization Tool")
    
    # Introduction to the tool
    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #e63946; margin-top: 0;">Margin Optimization Engine</h3>
        <p style="color: #CCC;">This advanced tool helps you determine optimal pricing strategies to maximize margins 
        based on market data, cost structures, and elasticity metrics. Input your product details below to receive 
        customized pricing recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input form in columns
    form_col1, form_col2 = st.columns(2)
    
    with form_col1:
        product_category = st.selectbox(
            "Product Category",
            options=["Denim Jeans", "Denim Jackets", "Denim Shirts", "T-Shirts", "Cargo Pants", "Other"]
        )
        
        base_cost = st.number_input(
            "Base Production Cost ($)",
            min_value=5.0,
            max_value=50.0,
            value=15.0,
            step=0.5
        )
        
        overhead_pct = st.slider(
            "Overhead & Operations (%)",
            min_value=5,
            max_value=40,
            value=20,
            step=5
        )
        
        shipping_cost = st.number_input(
            "Shipping & Logistics Cost ($)",
            min_value=1.0,
            max_value=10.0,
            value=2.5,
            step=0.5
        )
    
    with form_col2:
        target_market = st.selectbox(
            "Target Market",
            options=["Budget", "Mid-Range", "Premium", "Luxury"]
        )
        
        quantity = st.number_input(
            "Order Quantity",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100
        )
        
        marketing_pct = st.slider(
            "Marketing & Promotion (%)",
            min_value=0,
            max_value=25,
            value=10,
            step=5
        )
        
        season = st.selectbox(
            "Selling Season",
            options=["Spring/Summer", "Fall/Winter", "Year-round"]
        )
    
    # Action button
    if st.button("Calculate Optimal Pricing", type="primary", use_container_width=True):
        # Sample calculation logic
        total_cost = base_cost + (base_cost * overhead_pct / 100) + shipping_cost
        
        # Add marketing cost
        marketing_cost = total_cost * marketing_pct / 100
        total_cost += marketing_cost
        
        # Apply volume discount
        if quantity > 5000:
            volume_discount = 0.15
        elif quantity > 2000:
            volume_discount = 0.10
        elif quantity > 1000:
            volume_discount = 0.05
        else:
            volume_discount = 0
        
        total_cost = total_cost * (1 - volume_discount)
        
        # Target margins based on market
        if target_market == "Budget":
            target_margin = 0.25  # 25%
            price_sensitivity = 2.0
            market_positioning = "Budget"
        elif target_market == "Mid-Range":
            target_margin = 0.40  # 40%
            price_sensitivity = 1.5
            market_positioning = "Mid-Range"
        elif target_market == "Premium":
            target_margin = 0.60  # 60%
            price_sensitivity = 1.0
            market_positioning = "Premium"
        else:  # Luxury
            target_margin = 0.80  # 80%
            price_sensitivity = 0.7
            market_positioning = "Luxury"
        
        # Seasonal adjustment
        if season == "Spring/Summer":
            seasonal_factor = 1.05  # 5% premium
        elif season == "Fall/Winter":
            seasonal_factor = 1.10  # 10% premium
        else:  # Year-round
            seasonal_factor = 1.0
        
        # Calculate recommended prices
        min_viable_price = total_cost / (1 - target_margin * 0.6)
        target_price = total_cost / (1 - target_margin)
        premium_price = total_cost / (1 - target_margin * 1.2)
        
        # Apply seasonal adjustment
        min_viable_price *= seasonal_factor
        target_price *= seasonal_factor
        premium_price *= seasonal_factor
        
        # Round prices
        min_viable_price = round(min_viable_price, 2)
        target_price = round(target_price, 2)
        premium_price = round(premium_price, 2)
        
        # Display results
        st.markdown("---")
        st.markdown("### Pricing Recommendations")
        
        price_cols = st.columns(3)
        
        with price_cols[0]:
            st.markdown(f"""
            <div class="metric-container" style="border-left: 4px solid #F44336;">
                <div class="metric-title">Minimum Viable Price</div>
                <div class="metric-value" style="color: #F44336;">${min_viable_price:.2f}</div>
                <div class="metric-subtitle">Margin: {round((1 - total_cost/min_viable_price) * 100)}%</div>
            </div>
            """, unsafe_allow_html=True)
        
        with price_cols[1]:
            st.markdown(f"""
            <div class="metric-container" style="border-left: 4px solid #4CAF50;">
                <div class="metric-title">Target Price</div>
                <div class="metric-value" style="color: #4CAF50;">${target_price:.2f}</div>
                <div class="metric-subtitle">Margin: {round((1 - total_cost/target_price) * 100)}%</div>
            </div>
            """, unsafe_allow_html=True)
        
        with price_cols[2]:
            st.markdown(f"""
            <div class="metric-container" style="border-left: 4px solid #2196F3;">
                <div class="metric-title">Premium Price</div>
                <div class="metric-value" style="color: #2196F3;">${premium_price:.2f}</div>
                <div class="metric-subtitle">Margin: {round((1 - total_cost/premium_price) * 100)}%</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Cost breakdown
        st.markdown("### Cost Structure Analysis")
        
        cost_data = {
            "Cost Component": ["Base Production", "Overhead & Operations", "Shipping & Logistics", "Marketing & Promotion", "Total Cost"],
            "Amount": [
                f"${base_cost:.2f}",
                f"${base_cost * overhead_pct / 100:.2f}",
                f"${shipping_cost:.2f}",
                f"${marketing_cost:.2f}",
                f"${total_cost:.2f}"
            ],
            "Percentage": [
                f"{base_cost / total_cost * 100:.1f}%",
                f"{base_cost * overhead_pct / 100 / total_cost * 100:.1f}%",
                f"{shipping_cost / total_cost * 100:.1f}%",
                f"{marketing_cost / total_cost * 100:.1f}%",
                "100.0%"
            ]
        }
        
        cost_df = pd.DataFrame(cost_data)
        
        # Function to highlight the total row
        def highlight_total(row):
            if row["Cost Component"] == "Total Cost":
                return ['background-color: rgba(230, 57, 70, 0.1)'] * len(row)
            return [''] * len(row)
        
        st.dataframe(
            cost_df.style.apply(highlight_total, axis=1),
            use_container_width=True
        )
        
        # Create waterfall chart
        cost_breakdown = [
            {"name": "Base Production", "value": base_cost},
            {"name": "Overhead", "value": base_cost * overhead_pct / 100},
            {"name": "Shipping", "value": shipping_cost},
            {"name": "Marketing", "value": marketing_cost},
        ]
        
        fig = go.Figure(go.Waterfall(
            name="Cost Breakdown",
            orientation="v",
            measure=["relative", "relative", "relative", "relative", "total"],
            x=[item["name"] for item in cost_breakdown] + ["Total Cost"],
            y=[item["value"] for item in cost_breakdown] + [total_cost],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            increasing={"marker": {"color": "#1E3A8A"}},
            totals={"marker": {"color": "#e63946"}}
        ))
        
        fig.update_layout(
            title="Cost Structure Breakdown",
            showlegend=False,
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=60, b=40),
            font=dict(
                color="white"
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Margin analysis
        st.markdown("### Margin Analysis and Volume Projections")
        
        # Generate volume projections based on price elasticity
        prices = np.linspace(min_viable_price * 0.9, premium_price * 1.1, 20)
        base_volume = quantity
        
        # Calculate projected volume at different price points
        volumes = []
        for price in prices:
            # Price elasticity formula: % change in volume = price elasticity * % change in price
            price_diff_pct = (price - target_price) / target_price
            volume_change_pct = -1 * price_sensitivity * price_diff_pct
            projected_volume = base_volume * (1 + volume_change_pct)
            volumes.append(max(0, projected_volume))
        
        # Calculate revenue
        revenues = prices * np.array(volumes)
        
        # Calculate profit
        profits = (prices - total_cost) * np.array(volumes)
        
        # Create dataframe for visualization
        projection_df = pd.DataFrame({
            "Price": prices,
            "Volume": volumes,
            "Revenue": revenues,
            "Profit": profits,
            "Margin": (prices - total_cost) / prices * 100
        })
        
        # Find the optimal price for maximum profit
        max_profit_row = projection_df.loc[projection_df["Profit"].idxmax()]
        optimal_price = max_profit_row["Price"]
        optimal_margin = max_profit_row["Margin"]
        optimal_volume = max_profit_row["Volume"]
        optimal_profit = max_profit_row["Profit"]
        
        # Create visualizations
        fig = make_subplots(rows=1, cols=2, specs=[[{"type": "scatter"}, {"type": "scatter"}]])
        
        # Revenue and Profit vs Price
        fig.add_trace(
            go.Scatter(
                x=projection_df["Price"],
                y=projection_df["Revenue"],
                mode="lines",
                name="Revenue",
                line=dict(color="#1E3A8A", width=3)
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=projection_df["Price"],
                y=projection_df["Profit"],
                mode="lines",
                name="Profit",
                line=dict(color="#e63946", width=3)
            ),
            row=1, col=1
        )
        
        # Add vertical line at optimal price
        fig.add_vline(
            x=optimal_price,
            line_width=2,
            line_dash="dash",
            line_color="green",
            row=1,
            col=1
        )
        
        # Margin and Volume vs Price
        fig.add_trace(
            go.Scatter(
                x=projection_df["Price"],
                y=projection_df["Margin"],
                mode="lines",
                name="Margin %",
                line=dict(color="#43A047", width=3)
            ),
            row=1, col=2
        )
        
        fig.add_trace(
            go.Scatter(
                x=projection_df["Price"],
                y=projection_df["Volume"],
                mode="lines",
                name="Volume",
                line=dict(color="#FFA000", width=3),
                yaxis="y2"
            ),
            row=1, col=2
        )
        
        # Add vertical line at optimal price on second chart
        fig.add_vline(
            x=optimal_price,
            line_width=2,
            line_dash="dash",
            line_color="green",
            row=1,
            col=2
        )
        
        # Update layout
        fig.update_layout(
            title="Pricing Optimization Analysis",
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=60, b=40),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            font=dict(
                color="white"
            )
        )
        
        fig.update_xaxes(title_text="Price ($)", row=1, col=1)
        fig.update_xaxes(title_text="Price ($)", row=1, col=2)
        fig.update_yaxes(title_text="Revenue/Profit ($)", row=1, col=1)
        fig.update_yaxes(title_text="Margin (%)", row=1, col=2)
        
        # Add second y-axis for volume
        fig.update_layout(
            yaxis2=dict(
                title="Volume (Units)",
                anchor="x2",
                overlaying="y",
                side="right"
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Optimal pricing recommendation
        st.markdown("### Optimal Pricing Recommendation")
        
        recommendation_cols = st.columns([3, 1])
        
        with recommendation_cols[0]:
            st.markdown(f"""
            <div class="info-card" style="background-color: rgba(76, 175, 80, 0.1); border-left-color: #4CAF50;">
                <h4 style="color: #4CAF50; margin-top: 0;">Recommended Pricing Strategy</h4>
                <p>Based on your inputs and our market analysis, the optimal price point for 
                maximum profitability is <strong>${optimal_price:.2f}</strong> per unit. At this price:
                </p>
                <ul>
                    <li>Expected volume: {optimal_volume:.0f} units</li>
                    <li>Projected profit: ${optimal_profit:.2f}</li>
                    <li>Gross margin: {optimal_margin:.1f}%</li>
                </ul>
                <p>This represents the optimal balance between volume and margin for your specific product 
                and market positioning. The recommendation takes into account your cost structure, market position, 
                and price elasticity in the target segment.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Additional tips based on market
            if market_positioning == "Budget":
                st.info("Tip: In the budget segment, consider bundle pricing and volume discounts to maximize total sales value.")
            elif market_positioning == "Mid-Range":
                st.info("Tip: For mid-range products, emphasize value-to-price ratio in marketing to justify the premium over budget alternatives.")
            elif market_positioning == "Premium":
                st.info("Tip: Premium products benefit from tiered pricing strategies with 'good-better-best' options to capture different consumer segments.")
            else:  # Luxury
                st.info("Tip: For luxury positioning, consider limited editions and exclusivity to maintain premium positioning and price integrity.")
        
        with recommendation_cols[1]:
            # Show gauge chart for price optimization
            
            # Calculate how close the optimal price is to the target price
            diff_from_target = abs(optimal_price - target_price) / target_price
            
            if diff_from_target < 0.05:
                optimization_score = 95
                gauge_color = "#4CAF50"  # Green
            elif diff_from_target < 0.10:
                optimization_score = 85
                gauge_color = "#2196F3"  # Blue
            elif diff_from_target < 0.15:
                optimization_score = 75
                gauge_color = "#FFA000"  # Orange
            else:
                optimization_score = 65
                gauge_color = "#F44336"  # Red
            
            # Create gauge chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=optimization_score,
                title={"text": "Optimization Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": gauge_color},
                    "steps": [
                        {"range": [0, 50], "color": "rgba(244, 67, 54, 0.3)"},
                        {"range": [50, 75], "color": "rgba(255, 160, 0, 0.3)"},
                        {"range": [75, 90], "color": "rgba(33, 150, 243, 0.3)"},
                        {"range": [90, 100], "color": "rgba(76, 175, 80, 0.3)"}
                    ],
                    "threshold": {
                        "line": {"color": "white", "width": 2},
                        "thickness": 0.8,
                        "value": optimization_score
                    }
                }
            ))
            
            fig.update_layout(
                height=250,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=20, r=20, t=50, b=20),
                font=dict(
                    color="white"
                )
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Show comparison to target price
            price_diff = ((optimal_price - target_price) / target_price) * 100
            
            if abs(price_diff) < 5:
                diff_text = "close to"
                diff_color = "#4CAF50"
            elif price_diff > 0:
                diff_text = f"{price_diff:.1f}% higher than"
                diff_color = "#F44336" if price_diff > 10 else "#FFA000"
            else:
                diff_text = f"{abs(price_diff):.1f}% lower than"
                diff_color = "#F44336" if abs(price_diff) > 10 else "#FFA000"
            
            st.markdown(f"""
            <div style="background-color: #212121; padding: 15px; border-radius: 10px; margin-top: 10px;">
                <p style="margin: 0; font-size: 0.9em;">Optimal price is <span style="color: {diff_color};">{diff_text}</span> your target price of <strong>${target_price:.2f}</strong></p>
            </div>
            """, unsafe_allow_html=True)

# Helper function for margin optimizer
def make_subplots(rows=1, cols=1, specs=None):
    """Simple implementation of plotly's make_subplots for demonstration"""
    fig = go.Figure()
    fig.rows = rows
    fig.cols = cols
    fig.specs = specs
    return fig