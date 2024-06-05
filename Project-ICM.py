import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import re

# Set the page configuration with the Airbnb icon
st.set_page_config(page_title='Industial Copper Price Prediction Model', page_icon="C:/Users/SANTHOSH RAJENDRAN\Desktop/GUVI Python/Project-ICM/ICM.jpg", layout="wide")

# Front Page Design
st.markdown("<h1 style='text-align: center; font-weight: bold; font-family: Comic Sans MS;'>Industrial Copper Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Hello Connections! 👋 Welcome to My Project Presentation 🙏</h3>", unsafe_allow_html=True)

selected_page = option_menu(
    menu_title='',
    options=["Home","Prediction Zone","About"],
    icons=["house","trophy","patch-question"],
    default_index=1,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "gold","size":"cover", "width": "100"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "15px", "text-align": "center", "margin": "-2px", "--hover-color": "#white"},
            "nav-link-selected": {"background-color": "green"}})

if selected_page == "About":
    st.header(" :Green[Project Conclusion]")
    tab1,tab2 = st.tabs(["Features","Connect with me on"])
    with tab1:
        st.header("This Streamlit application allows users to access and analyze data from dataset.", divider='rainbow')
        st.subheader("1.    Users can select specific criteria such as Quantity, Product Type, Item Type, Country, Thickness, and Width to retrieve relevant data and analyze trends.")
        st.subheader("2.    Users can access slicers and filters to explore data. They can customize the filters based on their preferences.")
        st.subheader("3.    The analysis zone provides users with access to filters derived through Python scripting.")
        st.subheader("4.    They can explore advanced predicted values to gain deeper insights into dataset.")
    with tab2:
             # Create buttons to direct to different website
            linkedin_button = st.button("LinkedIn")
            if linkedin_button:
                st.write("[Redirect to LinkedIn Profile > (https://www.linkedin.com/in/santhosh-r-42220519b/)](https://www.linkedin.com/in/santhosh-r-42220519b/)")

            email_button = st.button("Email")
            if email_button:
                st.write("[Redirect to Gmail > santhoshsrajendran@gmail.com](santhoshsrajendran@gmail.com)")

            github_button = st.button("GitHub")
            if github_button:
                st.write("[Redirect to Github Profile > https://github.com/Santhosh-1703](https://github.com/Santhosh-1703)")

elif selected_page == "Prediction Zone":
    tab1, tab2 = st.tabs(["PREDICT SELLING PRICE", "PREDICT STATUS"])
    

    # Define options and mappings
    status_options = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
    item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
    country_options = [28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
    application_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
    product=['611112', '611728', '628112', '628117', '628377', '640400', '640405', '640665', 
                '611993', '929423819', '1282007633', '1332077137', '164141591', '164336407', 
                '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', 
                '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', 
                '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']

    with tab1:
        with st.form("my_form"):
            col1, col2, col3 = st.columns([5, 2, 5])
            with col1:
                status_code = {'Won':1, 'Draft':2, 'To be approved':3, 'Lost':0, 'Not lost for AM':5, 'Wonderful':6, 'Revised':7, 'Offered':8, 'Offerable':4}
                cc = {'W':5, 'WI':6, 'S':3, 'Others':1, 'PL':2, 'IPL':0, 'SLAWR':4}
                country_options = [28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89]
                application_options = [2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 19.0, 20.0, 22.0, 25.0, 26.0, 
                                        27.0, 28.0, 29.0, 38.0, 39.0, 40.0, 41.0, 42.0, 56.0, 58.0, 
                                        59.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 79.0, 99.0]
                product=[1670798778,     611993, 1668701376,  164141591,     628377,
                                1671863738,     640665, 1332077137, 1668701718,     640405,
                                1693867550, 1665572374, 1282007633, 1668701698,     628117,
                                1690738206,     640400, 1671876026,     628112,  164336407,
                                    164337175, 1668701725, 1665572032,     611728, 1721130331,
                                1693867563,     611733, 1690738219, 1722207579, 1665584662,
                                1665584642,  929423819, 1665584320]
                st.write(' ')
                status = st.selectbox("Status", status_code)
                qt = st.slider("Quantity Tons (Min: 0.1, Max: 1722207579.0)", 611728.0, 1722207579.0) 
                quantity_tons = np.log(qt)  
                country = st.selectbox("Country", sorted(country_options))
                width = st.slider("Width (Min: 1, Max: 2990.000000)", 1.0, 2990.000000)   
                product_ref = st.selectbox("Product Reference", product)
            with col3:
                item_type = st.selectbox("Item Type", cc)
                tq = st.slider("Thickness (Min: 0.18, Max: 2500.000000)", 0.18, 2500.000000)
                thickness = np.log(tq)
                application = st.selectbox("Application", sorted(application_options),key=4)
                customer = st.slider("Customer ID (Min: 12458, Max: 2147483647.0)", 12458.0, 2147483647.0, step=1.0)
                submit_button = st.form_submit_button(label="PREDICT SELLING PRICE")
            
            flag = 0
            pattern = "^(?:\d+|\d*\.\d+)$"
            for i in [quantity_tons, thickness, width, customer]:
                if re.match(pattern, str(i)):
                    pass
                else:
                    flag = 1
                    break
            
            col1,col2,col3 = st.columns([10,2,10])     
            with col3 :

                if submit_button and flag == 1:
                    st.write("Please enter a valid number; spaces are not allowed.")

                if submit_button and flag == 0:
                        predict_data = [quantity_tons,customer,country,cc[item_type],application,
                                        thickness,width,product_ref,status_code[status]]
                        import pickle
                        with open(r"C:/Users/SANTHOSH RAJENDRAN/Desktop/GUVI Python/Project-ICM/regression_model.pkl", 'rb') as f:
                                    model = pickle.load(f)
                        
                        new_pred = model.predict([predict_data])
                        pred_price = np.exp(new_pred[0])
                        rounded_pred = round(pred_price, 2) # Round to 2 decimal placescol1,col2 = st.columns([9,1])
                        col1,col2 = st.columns([9,1])
                        with col1 :
                            st.write(' ')
                            st.write(' ')
                            st.success(f'Predicted selling price 🪙: 💲 {rounded_pred}')

    with tab2:
         with st.form("my_form1"):
            col1, col2, col3 = st.columns([5, 2, 5])
            with col1:
                status_code = {'Won':1, 'Draft':2, 'To be approved':3, 'Lost':0, 'Not lost for AM':5, 'Wonderful':6, 'Revised':7, 'Offered':8, 'Offerable':4}
                cc = {'W':5, 'WI':6, 'S':3, 'Others':1, 'PL':2, 'IPL':0, 'SLAWR':4}
                country_options = [28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89]
                application_options = [2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 19.0, 20.0, 22.0, 25.0, 26.0, 
                                        27.0, 28.0, 29.0, 38.0, 39.0, 40.0, 41.0, 42.0, 56.0, 58.0, 
                                        59.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 79.0, 99.0]
                product=[1670798778,     611993, 1668701376,  164141591,     628377,
                                1671863738,     640665, 1332077137, 1668701718,     640405,
                                1693867550, 1665572374, 1282007633, 1668701698,     628117,
                                1690738206,     640400, 1671876026,     628112,  164336407,
                                    164337175, 1668701725, 1665572032,     611728, 1721130331,
                                1693867563,     611733, 1690738219, 1722207579, 1665584662,
                                1665584642,  929423819, 1665584320]
                st.write(' ')
                sp = st.slider("Select Selling Price (Min: 1.0, Max: 100001015.0)", 1.0, 100001015.0) 
                selling_price = np.log(sp) 
                qt = st.slider("Quantity Tons (Min: 0.1, Max: 1722207579.0)", 611728.0, 1722207579.0) 
                quantity_tons = np.log(qt)  
                country = st.selectbox("Country", sorted(country_options))
                width = st.slider("Width (Min: 1, Max: 2990.000000)", 1.0, 2990.000000)   
                product_ref = st.selectbox("Product Reference", product)
            with col3:
                item_type = st.selectbox("Item Type", cc)
                tq = st.slider("Thickness (Min: 0.18, Max: 2500.000000)", 0.18, 2500.000000)
                thickness = np.log(tq)
                application = st.selectbox("Application", sorted(application_options))
                customer = st.slider("Customer ID (Min: 12458, Max: 2147483647.0)", 12458.0, 2147483647.0, step=1.0)
                submit_button = st.form_submit_button(label="PREDICT STATUS")
            
                predict_data = [quantity_tons,customer,country,cc[item_type],application,thickness,width,product_ref,
                                        selling_price]
                import pickle
                
                with open("C:/Users/SANTHOSH RAJENDRAN/Desktop/GUVI Python/Project-ICM/classification_model_icm.pkl", 'rb') as f:
                            model = pickle.load(f)
                
                st.write("")
                if submit_button:
                        x = model.predict([predict_data])
                        if x[0] == 1.0:
                            st.success(f'Predicted Status : 👍 Won')
                                
                        elif x[0] == 0.0:
                            st.warning(f'Predicted Status : 👎 Lost')

elif selected_page == "Home":
    tab1,tab2 = st.tabs(["Copper Price Model Prediction","  Applications and Libraries Used! "])
    with tab1:
        st.write(" Copper Price Prediction using a Machine Learning helps organizations gather valuable insights about Total Performing Hotels, Customer Reviews, and Property details. By combining this data with information from social media, organizations can get a comprehensive view of their online presence and audience engagement. This approach enables data-driven decision-making and more effective content strategies.")
        st.write("[:open_book: Click here to know current Copper Price  >](https://markets.businessinsider.com/commodities/copper-price)")
        if st.button("Click here to know about this Model"):
            col1, col2 = st.columns(2)
            with col1:
                st.image(r"C:\Users\SANTHOSH RAJENDRAN\Desktop\GUVI Python\Project-ICM\ivideo.jpg",width=500)
            with col2:
                st.header(':white[Application info]', divider='rainbow')
                st.subheader(":star: Industrial Copper Modelling Project involves to predict both Price & Status of Particular Copper type")
                st.subheader(":star: To predict the Copper Price, Regression Trained Model is used. ")
                st.subheader(":star: To predict the Copper Price Status, Classification Trained Model is used ")
            
    with tab2:
                st.subheader("  :bulb: Python")
                st.subheader("  :bulb: Numpy")
                st.subheader("  :bulb: Pandas")
                st.subheader("  :bulb: Scikit-Learn")
                st.subheader("  :bulb: Streamlit")
     
    
                    
                