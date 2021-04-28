'''
linearerror.py

- Written on 2/13/2018 for CLaSP 405 by Lab TA A. Azari.
- Modified on 2/11/2020 for CLaSP 405 by Lab TA B. Swiger.
Purpose:
- To calculate with x and y the error on the coefficents
as demonstrated in eqn. 8.15, 8.16, 8.17 in Taylor - 
An Introduction to Error Analysis.

'''

def calc_coeffs_error(x, rmse):
    '''
    This function calculates the error on the coefficents or
    equation 8.16 & 8.17 in Taylor. Inputs are the x values 
    of the equation and the RMSE on the fit. 

    Outputs the error on the slope, THEN on the intercept. 

    '''
    import numpy as np
    
    delta = len(x)*sum(x**2) - (sum(x)**2)

    slope_error = rmse * np.sqrt((len(x)) / delta)
    intercept_error = rmse * np.sqrt(sum((x**2)) / delta)
    
    return(slope_error, intercept_error)
    
def calc_rmse(y_model, y_data):
    '''
    This calculates sigma y, or equation 8.15 in Taylor. Outputs
    error on the fit of regressions. 
    '''
    import numpy as np
    
    sum_of_squared_error = sum(((y_model - y_data)**2))
    mean_squared_error = (sum_of_squared_error / (len(y_model) - 2.0))
    
    return(np.sqrt(mean_squared_error))
