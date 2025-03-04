import streamlit as st

st.title ('Unit Convertor')
st.write('Convert units into length , weight and time')

st.write('Convert units')
category = st.selectbox('Choose catagory' ,['Length' , 'Weight' , 'Time'])

def unit_convert(catagory , unit , value):

    # ============ Length convertor==========
    if catagory == 'Length':
      if unit == 'Kilometers to miles':
         return value * 0.621371
      elif unit == 'miles to Kilometers':
         return value / 0.621371
      
      # ============== weight convertor =========

    if catagory == 'Weight':
      if unit == 'Kilograms to grams':
         return value * 1000
      elif unit == 'grams to Kilograms':
         return value / 1000
      
      elif unit == 'Kilograms to pounds':
         return value * 2.20462
      elif unit == 'pounds to Kilograms':
         return value / 2.20462
      
      # ============== Time convertor ===========

    if catagory == 'Time':
      if unit == 'Days to hours':
            return value * 24
      elif unit == 'hours to Days':
            return value / 24
         
      elif unit == 'seconds to minutes':
            return value / 60
      elif unit == 'minutes to seconds':
            return value * 60
         
      elif unit == 'minutes to hours':
            return value / 60
      elif unit == 'hours to minutes':
            return value * 60
    
        
         
if category == 'Length':
   unit = st.selectbox('Select conversion' , ['Kilometers to miles' , 'miles to Kilometers' ])
elif category == 'Weight':
    unit = st.selectbox ("Select conversion" , ['Kilograms to grams' , 'grams to Kilograms' , 'Kilograms to pounds' , 'pounds to Kilograms'])
elif category == 'Time':
    unit = st.selectbox("Select conversion" , ['Days to hours' , 'hours to Days' , 'seconds to minutes' , 'minutes to hours' , 'hours to minutes'])


#  ============ Button to convert  the units ===========

value = st.number_input('Enter value')

if st.button ('Convert'):
   result = unit_convert( category , unit , value)
   st.success(f'The result is {result:.2f}')         

      



