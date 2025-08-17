# 💰 Fund Administration System Demo

A comprehensive Streamlit-based demo application for fund administration, featuring dashboard analytics, onboarding workflows, and compliance management.

## 🚀 Features

### 📊 Dashboard Overview
- **Real-time Metrics**: Total AUM, investor count, active funds, and pending approvals
- **Interactive Charts**: Fund performance tracking and AUM distribution
- **Activity Feed**: Recent system activities and status updates
- **Fund Overview Table**: Complete fund information display

### 📝 Onboarding Workflows
- **Fund Onboarding**: Complete fund registration with legal and risk information
- **Client Onboarding**: Personal and financial profile creation
- **Person Onboarding**: Professional background and certification tracking
- **Investor Onboarding**: Investment preferences and documentation verification

### 🔒 Compliance & KYC
- **AML/KYC Dashboard**: Application status tracking and risk assessment
- **Risk Level Distribution**: Visual representation of client risk profiles
- **Compliance Timeline**: Monthly application and approval trends

### 🔗 Relationship Management
- **Fund/Company Relationships**: Service provider and administrator tracking
- **Individual/Fund Relationships**: Investor and staff relationship management

## 🛠️ Installation

1. **Clone or download the project files**
   ```bash
   # Make sure you have the following files:
   # - Home.py
   # - requirements.txt
   # - README.md
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**
   ```bash
   streamlit run Home.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in your terminal

## 📋 Requirements

- Python 3.8 or higher
- Streamlit 1.28.1
- Pandas 2.1.3
- Plotly 5.17.0
- Other dependencies listed in `requirements.txt`

## 🎯 Usage Guide

### Navigation
- Use the sidebar navigation to switch between different sections
- Each section provides specific functionality for fund administration tasks

### Dashboard
- View key performance indicators and fund metrics
- Interact with charts to explore fund performance data
- Monitor recent activities and system status

### Onboarding Forms
- Fill out comprehensive forms for different entity types
- All forms include validation and user-friendly interfaces
- Submit applications and receive confirmation messages

### Compliance
- Track KYC application status
- View risk assessment analytics
- Monitor compliance trends and metrics

## 🎨 Design Features

- **Modern UI**: Clean, professional interface with gradient backgrounds
- **Responsive Layout**: Optimized for different screen sizes
- **Interactive Elements**: Hover effects and smooth transitions
- **Color-coded Status**: Visual indicators for different status types
- **Professional Styling**: Consistent branding and typography

## 📊 Sample Data

The application includes realistic sample data for demonstration purposes:
- 4 sample funds with varying AUM and investor counts
- Performance data with realistic market fluctuations
- Sample investor profiles and KYC applications
- Activity logs and compliance metrics

## 🔧 Customization

### Adding New Features
1. Extend the navigation menu in the sidebar
2. Add new page conditions in the main content area
3. Create corresponding form components or data displays

### Styling Modifications
- Edit the CSS in the `st.markdown` section at the top of `Home.py`
- Modify color schemes, fonts, and layout properties
- Add custom components and styling

### Data Integration
- Replace sample data functions with real database connections
- Implement API integrations for external data sources
- Add data persistence and user authentication

## 🚨 Important Notes

- This is a **demo application** for educational and demonstration purposes
- All data is sample data and not connected to real financial systems
- No actual financial transactions or sensitive data processing occurs
- Suitable for showcasing fund administration workflows and UI/UX concepts

## 📞 Support

For questions or issues with the demo application:
1. Check the Streamlit documentation: https://docs.streamlit.io/
2. Review the code comments for implementation details
3. Ensure all dependencies are properly installed

## 📄 License

This demo application is provided as-is for educational purposes. Feel free to modify and extend it for your specific needs.

---

**Built with ❤️ using Streamlit**
