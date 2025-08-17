import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="Fund Administration System",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #0c4a6e 0%, #145374 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #e8f0fc 0%, #cce0ff 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #0c4a6e;
        margin: 0.5rem 0;
    }
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .stButton > button {
        background: linear-gradient(90deg, #0c4a6e 0%, #145374 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #145374 0%, #1e729f 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'

# Sample data generation
def generate_sample_data():
    # Fund data
    funds_data = {
        'Fund Name': ['Alpha Growth Fund', 'Beta Income Fund', 'Gamma Tech Fund', 'Delta Balanced Fund'],
        'AUM (Million $)': [1250, 890, 2100, 750],
        'Investors': [45, 32, 78, 28],
        'Status': ['Active', 'Active', 'Active', 'Pending'],
        'Launch Date': ['2020-01-15', '2019-06-20', '2021-03-10', '2023-11-01']
    }
    
    # Performance data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
    performance_data = {
        'Date': dates,
        'Alpha Growth': [100] + [100 + i*2 + random.uniform(-5, 5) for i in range(len(dates)-1)],
        'Beta Income': [100] + [100 + i*1.5 + random.uniform(-3, 3) for i in range(len(dates)-1)],
        'Gamma Tech': [100] + [100 + i*3 + random.uniform(-8, 8) for i in range(len(dates)-1)],
        'Delta Balanced': [100] + [100 + i*1.8 + random.uniform(-4, 4) for i in range(len(dates)-1)]
    }
    
    # Investor data
    investors_data = {
        'Investor Name': ['John Smith', 'Sarah Johnson', 'Michael Brown', 'Emily Davis', 'David Wilson'],
        'Investment Amount ($)': [500000, 750000, 300000, 1200000, 450000],
        'Fund': ['Alpha Growth Fund', 'Beta Income Fund', 'Gamma Tech Fund', 'Alpha Growth Fund', 'Delta Balanced Fund'],
        'Status': ['Active', 'Active', 'Pending', 'Active', 'Active']
    }
    
    return pd.DataFrame(funds_data), pd.DataFrame(performance_data), pd.DataFrame(investors_data)

# Sidebar navigation
st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #0c4a6e 0%, #145374 100%); padding: 1rem; border-radius: 10px; margin-bottom: 2rem;">
    <h2 style="color: white; text-align: center; margin: 0;">💰 Fund Admin System</h2>
</div>
""", unsafe_allow_html=True)

# Navigation menu
st.sidebar.markdown("### 📊 Dashboard")

# Dashboard link
if st.sidebar.button("🏠 Dashboard Overview", key="dashboard_btn", help="View main dashboard"):
    st.session_state.current_page = 'Dashboard'

st.sidebar.markdown("### 📝 Onboarding")
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("🏦 Fund Onboarding", key="fund_btn", help="Fund Onboarding"):
        st.session_state.current_page = 'Fund Onboarding'
with col2:
    if st.button("👥 Client Onboarding", key="client_btn", help="Client Onboarding"):
        st.session_state.current_page = 'Client Onboarding'

col3, col4 = st.sidebar.columns(2)
with col3:
    if st.button("👤 Person Onboarding", key="person_btn", help="Person Onboarding"):
        st.session_state.current_page = 'Person Onboarding'
with col4:
    if st.button("💼 Investor Onboarding", key="investor_btn", help="Investor Onboarding"):
        st.session_state.current_page = 'Investor Onboarding'

st.sidebar.markdown("### 🔒 Compliance & KYC")
if st.sidebar.button("🛡️ AML / KYC", key="aml_btn", help="AML / KYC Compliance"):
    st.session_state.current_page = 'AML / KYC'

st.sidebar.markdown("### 🔗 Relationships")
col5, col6 = st.sidebar.columns(2)
with col5:
    if st.button("🏢 Fund/Company", key="fund_company_btn", help="Fund/Company Relationship"):
        st.session_state.current_page = 'Fund/Company Relationship'
with col6:
    if st.button("🤝 Individual/Fund", key="indiv_fund_btn", help="Individual/Fund Relationship"):
        st.session_state.current_page = 'Individual/Fund Relationship'

# Main content area
if st.session_state.current_page == 'Dashboard':
    st.markdown('<div class="main-header"><h1>📊 Dashboard Overview</h1></div>', unsafe_allow_html=True)
    
    # Generate sample data
    funds_df, performance_df, investors_df = generate_sample_data()
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>💰 Total AUM</h3>
            <h2>${funds_df['AUM (Million $)'].sum():,.0f}M</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>👥 Total Investors</h3>
            <h2>{funds_df['Investors'].sum()}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📈 Active Funds</h3>
            <h2>{len(funds_df[funds_df['Status'] == 'Active'])}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>⏳ Pending Approvals</h3>
            <h2>{len(funds_df[funds_df['Status'] == 'Pending'])}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Fund Performance")
        fig_performance = go.Figure()
        for fund in ['Alpha Growth', 'Beta Income', 'Gamma Tech', 'Delta Balanced']:
            fig_performance.add_trace(go.Scatter(
                x=performance_df['Date'],
                y=performance_df[fund],
                mode='lines+markers',
                name=fund,
                line=dict(width=2)
            ))
        fig_performance.update_layout(
            height=400,
            showlegend=True,
            xaxis_title="Date",
            yaxis_title="Performance Index"
        )
        st.plotly_chart(fig_performance, use_container_width=True)
    
    with col2:
        st.subheader("💰 AUM Distribution")
        fig_aum = px.pie(
            funds_df, 
            values='AUM (Million $)', 
            names='Fund Name',
            title="Assets Under Management by Fund"
        )
        fig_aum.update_layout(height=400)
        st.plotly_chart(fig_aum, use_container_width=True)
    
    # Fund table
    st.subheader("📋 Fund Overview")
    st.dataframe(funds_df, use_container_width=True)
    
    # Recent activities
    st.subheader("🔄 Recent Activities")
    activities = [
        {"Date": "2023-12-15", "Activity": "New investor onboarded to Alpha Growth Fund", "Status": "Completed"},
        {"Date": "2023-12-14", "Activity": "KYC verification completed for Sarah Johnson", "Status": "Completed"},
        {"Date": "2023-12-13", "Activity": "Delta Balanced Fund approval pending", "Status": "Pending"},
        {"Date": "2023-12-12", "Activity": "Quarterly report generated for Beta Income Fund", "Status": "Completed"},
        {"Date": "2023-12-11", "Activity": "AML check initiated for new client", "Status": "In Progress"}
    ]
    
    activities_df = pd.DataFrame(activities)
    st.dataframe(activities_df, use_container_width=True)

elif st.session_state.current_page == 'Fund Onboarding':
    st.markdown('<div class="main-header"><h1>📝 Fund Onboarding</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Fund Information")
            fund_name = st.text_input("Fund Name")
            fund_type = st.selectbox("Fund Type", ["Growth Fund", "Income Fund", "Balanced Fund", "Tech Fund", "Real Estate Fund"])
            investment_strategy = st.text_area("Investment Strategy")
            target_aum = st.number_input("Target AUM (Million $)", min_value=1, value=100)
        
        with col2:
            st.subheader("Legal Information")
            legal_entity = st.text_input("Legal Entity Name")
            jurisdiction = st.selectbox("Jurisdiction", ["Cayman Islands", "Luxembourg", "Ireland", "Singapore", "United States"])
            launch_date = st.date_input("Expected Launch Date")
            management_fee = st.number_input("Management Fee (%)", min_value=0.0, max_value=5.0, value=1.5, step=0.1)
        
        st.subheader("Risk Profile")
        risk_level = st.select_slider("Risk Level", options=["Conservative", "Moderate", "Aggressive"], value="Moderate")
        
        col3, col4 = st.columns(2)
        with col3:
            min_investment = st.number_input("Minimum Investment ($)", min_value=1000, value=100000)
            lock_period = st.number_input("Lock Period (Months)", min_value=0, value=12)
        
        with col4:
            redemption_frequency = st.selectbox("Redemption Frequency", ["Monthly", "Quarterly", "Semi-annually", "Annually"])
            subscription_frequency = st.selectbox("Subscription Frequency", ["Daily", "Weekly", "Monthly", "Quarterly"])
        
        if st.button("Submit Fund Application", type="primary"):
            st.success("✅ Fund onboarding application submitted successfully!")
            st.info("Your application will be reviewed within 3-5 business days.")
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'Client Onboarding':
    st.markdown('<div class="main-header"><h1>👥 Client Onboarding</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Personal Information")
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            date_of_birth = st.date_input("Date of Birth")
        
        with col2:
            st.subheader("Address Information")
            address_line1 = st.text_input("Address Line 1")
            address_line2 = st.text_input("Address Line 2")
            city = st.text_input("City")
            state = st.text_input("State/Province")
            postal_code = st.text_input("Postal Code")
            country = st.selectbox("Country", ["United States", "Canada", "United Kingdom", "Germany", "France", "Australia"])
        
        st.subheader("Financial Information")
        col3, col4 = st.columns(2)
        
        with col3:
            annual_income = st.selectbox("Annual Income Range", ["$0-$50,000", "$50,001-$100,000", "$100,001-$250,000", "$250,001-$500,000", "$500,001+"])
            net_worth = st.selectbox("Net Worth Range", ["$0-$100,000", "$100,001-$500,000", "$500,001-$1,000,000", "$1,000,001-$5,000,000", "$5,000,001+"])
        
        with col4:
            investment_experience = st.selectbox("Investment Experience", ["Beginner", "Intermediate", "Advanced", "Professional"])
            risk_tolerance = st.select_slider("Risk Tolerance", options=["Conservative", "Moderate", "Aggressive"], value="Moderate")
        
        st.subheader("Investment Preferences")
        investment_goals = st.multiselect("Investment Goals", ["Capital Preservation", "Income Generation", "Capital Growth", "Tax Efficiency", "Diversification"])
        preferred_funds = st.multiselect("Preferred Fund Types", ["Growth Funds", "Income Funds", "Balanced Funds", "Tech Funds", "Real Estate Funds"])
        
        if st.button("Submit Client Application", type="primary"):
            st.success("✅ Client onboarding application submitted successfully!")
            st.info("KYC verification will be initiated within 24 hours.")
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'Person Onboarding':
    st.markdown('<div class="main-header"><h1>👤 Person Onboarding</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Personal Details")
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            date_of_birth = st.date_input("Date of Birth")
            nationality = st.selectbox("Nationality", ["US Citizen", "Canadian", "UK Citizen", "German", "French", "Other"])
        
        with col2:
            st.subheader("Professional Information")
            job_title = st.text_input("Job Title")
            company = st.text_input("Company")
            industry = st.selectbox("Industry", ["Finance", "Technology", "Healthcare", "Real Estate", "Manufacturing", "Other"])
            years_experience = st.number_input("Years of Experience", min_value=0, value=5)
        
        st.subheader("Address Information")
        col3, col4 = st.columns(2)
        
        with col3:
            address_line1 = st.text_input("Address Line 1")
            address_line2 = st.text_input("Address Line 2")
            city = st.text_input("City")
        
        with col4:
            state = st.text_input("State/Province")
            postal_code = st.text_input("Postal Code")
            country = st.selectbox("Country", ["United States", "Canada", "United Kingdom", "Germany", "France", "Australia"])
        
        st.subheader("Additional Information")
        education_level = st.selectbox("Education Level", ["High School", "Bachelor's Degree", "Master's Degree", "PhD", "Professional Certification"])
        certifications = st.multiselect("Professional Certifications", ["CFA", "CPA", "CAIA", "FRM", "PMP", "None"])
        
        if st.button("Submit Person Application", type="primary"):
            st.success("✅ Person onboarding application submitted successfully!")
            st.info("Background verification will be completed within 5-7 business days.")
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'Investor Onboarding':
    st.markdown('<div class="main-header"><h1>💼 Investor Onboarding</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Investor Information")
            investor_type = st.selectbox("Investor Type", ["Individual", "Institutional", "Family Office", "Pension Fund", "Endowment"])
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
        
        with col2:
            st.subheader("Investment Details")
            target_fund = st.selectbox("Target Fund", ["Alpha Growth Fund", "Beta Income Fund", "Gamma Tech Fund", "Delta Balanced Fund"])
            investment_amount = st.number_input("Investment Amount ($)", min_value=10000, value=100000, step=10000)
            investment_source = st.selectbox("Source of Funds", ["Personal Savings", "Inheritance", "Business Proceeds", "Investment Returns", "Other"])
        
        st.subheader("Financial Profile")
        col3, col4 = st.columns(2)
        
        with col3:
            annual_income = st.selectbox("Annual Income Range", ["$0-$50,000", "$50,001-$100,000", "$100,001-$250,000", "$250,001-$500,000", "$500,001+"])
            net_worth = st.selectbox("Net Worth Range", ["$0-$100,000", "$100,001-$500,000", "$500,001-$1,000,000", "$1,000,001-$5,000,000", "$5,000,001+"])
        
        with col4:
            investment_experience = st.selectbox("Investment Experience", ["Beginner", "Intermediate", "Advanced", "Professional"])
            risk_tolerance = st.select_slider("Risk Tolerance", options=["Conservative", "Moderate", "Aggressive"], value="Moderate")
        
        st.subheader("Documentation")
        kyc_completed = st.checkbox("KYC Documentation Completed")
        aml_check = st.checkbox("AML Check Completed")
        suitability_assessment = st.checkbox("Suitability Assessment Completed")
        
        if st.button("Submit Investor Application", type="primary"):
            if kyc_completed and aml_check and suitability_assessment:
                st.success("✅ Investor onboarding application submitted successfully!")
                st.info("Your investment will be processed within 2-3 business days.")
            else:
                st.error("❌ Please complete all required documentation before submitting.")
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'AML / KYC':
    st.markdown('<div class="main-header"><h1>🔒 AML / KYC Compliance</h1></div>', unsafe_allow_html=True)
    
    # KYC Status Overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📋 Total Applications</h3>
            <h2>156</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>✅ Approved</h3>
            <h2>142</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>⏳ Pending Review</h3>
            <h2>8</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>❌ Rejected</h3>
            <h2>6</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # KYC Applications Table
    st.subheader("📋 KYC Applications")
    
    kyc_data = {
        'Applicant Name': ['John Smith', 'Sarah Johnson', 'Michael Brown', 'Emily Davis', 'David Wilson'],
        'Application Date': ['2023-12-10', '2023-12-11', '2023-12-12', '2023-12-13', '2023-12-14'],
        'Status': ['Approved', 'Pending', 'Approved', 'Rejected', 'Pending'],
        'Risk Level': ['Low', 'Medium', 'Low', 'High', 'Medium'],
        'Documents': ['Complete', 'Pending', 'Complete', 'Incomplete', 'Pending']
    }
    
    kyc_df = pd.DataFrame(kyc_data)
    st.dataframe(kyc_df, use_container_width=True)
    
    # Risk Assessment
    st.subheader("🎯 Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Risk distribution chart
        risk_data = {'Risk Level': ['Low', 'Medium', 'High'], 'Count': [85, 45, 26]}
        risk_df = pd.DataFrame(risk_data)
        fig_risk = px.bar(risk_df, x='Risk Level', y='Count', color='Risk Level',
                         color_discrete_map={'Low': '#28a745', 'Medium': '#ffc107', 'High': '#dc3545'})
        fig_risk.update_layout(height=300, title="Risk Level Distribution")
        st.plotly_chart(fig_risk, use_container_width=True)
    
    with col2:
        # Compliance timeline
        timeline_data = {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Applications': [12, 18, 15, 22, 19, 25],
            'Approvals': [10, 16, 14, 20, 18, 23]
        }
        timeline_df = pd.DataFrame(timeline_data)
        fig_timeline = go.Figure()
        fig_timeline.add_trace(go.Scatter(x=timeline_df['Month'], y=timeline_df['Applications'], 
                                        mode='lines+markers', name='Applications'))
        fig_timeline.add_trace(go.Scatter(x=timeline_df['Month'], y=timeline_df['Approvals'], 
                                        mode='lines+markers', name='Approvals'))
        fig_timeline.update_layout(height=300, title="Monthly KYC Applications vs Approvals")
        st.plotly_chart(fig_timeline, use_container_width=True)

elif st.session_state.current_page == 'Fund/Company Relationship':
    st.markdown('<div class="main-header"><h1>🔗 Fund / Company Relationship</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Fund Information")
            fund_name = st.selectbox("Fund Name", ["Alpha Growth Fund", "Beta Income Fund", "Gamma Tech Fund", "Delta Balanced Fund"])
            fund_manager = st.text_input("Fund Manager")
            fund_administrator = st.text_input("Fund Administrator")
        
        with col2:
            st.subheader("Company Information")
            company_name = st.text_input("Company Name")
            company_type = st.selectbox("Company Type", ["Investment Manager", "Administrator", "Custodian", "Auditor", "Legal Counsel"])
            relationship_type = st.selectbox("Relationship Type", ["Primary", "Secondary", "Advisory", "Service Provider"])
        
        st.subheader("Relationship Details")
        col3, col4 = st.columns(2)
        
        with col3:
            start_date = st.date_input("Relationship Start Date")
            contract_value = st.number_input("Contract Value ($)", min_value=0, value=50000)
        
        with col4:
            renewal_date = st.date_input("Contract Renewal Date")
            status = st.selectbox("Status", ["Active", "Pending", "Terminated", "Under Review"])
        
        st.subheader("Services Provided")
        services = st.multiselect("Services", ["Fund Administration", "Custody Services", "Audit Services", "Legal Services", "Compliance Monitoring", "Risk Management"])
        
        if st.button("Submit Relationship", type="primary"):
            st.success("✅ Fund/Company relationship recorded successfully!")
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'Individual/Fund Relationship':
    st.markdown('<div class="main-header"><h1>👤 Individual / Fund Relationship</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Individual Information")
            individual_name = st.text_input("Individual Name")
            individual_type = st.selectbox("Individual Type", ["Investor", "Fund Manager", "Board Member", "Advisor", "Employee"])
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
        
        with col2:
            st.subheader("Fund Information")
            fund_name = st.selectbox("Fund Name", ["Alpha Growth Fund", "Beta Income Fund", "Gamma Tech Fund", "Delta Balanced Fund"])
            role_in_fund = st.selectbox("Role in Fund", ["Investor", "Fund Manager", "Board Member", "Advisor", "Employee"])
            start_date = st.date_input("Start Date")
        
        st.subheader("Relationship Details")
        col3, col4 = st.columns(2)
        
        with col3:
            investment_amount = st.number_input("Investment Amount ($)", min_value=0, value=100000)
            ownership_percentage = st.number_input("Ownership Percentage (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
        
        with col4:
            voting_rights = st.checkbox("Voting Rights")
            board_seat = st.checkbox("Board Seat")
        
        st.subheader("Additional Information")
        compensation_type = st.selectbox("Compensation Type", ["Salary", "Performance Fee", "Management Fee", "Carried Interest", "None"])
        reporting_frequency = st.selectbox("Reporting Frequency", ["Monthly", "Quarterly", "Semi-annually", "Annually"])
        
        if st.button("Submit Relationship", type="primary"):
            st.success("✅ Individual/Fund relationship recorded successfully!")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>💰 Fund Administration System Demo | Built with Streamlit</p>
    <p>This is a demonstration application for educational purposes.</p>
</div>
""", unsafe_allow_html=True)
