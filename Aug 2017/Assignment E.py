# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:31:11 2019

@author: HP
"""
import numpy as np
def costliestCar(maxPrice):
   
    BasePrice = 159000
    TrimPrice = np.array([0, 22000, 44000])
    ExtraPrice = np.array([4000, 8000, 13000, 7000])

   
    TrimString = np.array(["Access", "Comfort", "Sport"])
    ExtraString = np.array(["Cruise control", "Air conditioning", "Alloy wheels", "Chrome spoiler"])

    
    costliestPrice = 0

    # Loop over all trim levels
    for trim in range(3):
        # Loop over all combinations of extras
        for extra in range(2**4):
    	    # Binary indicator of extras
            extra_indicator = np.floor(extra / 2**np.arange(4)) % 2 == 1

            # Compute price
            price = BasePrice + TrimPrice[trim] + np.sum(ExtraPrice[extra_indicator])

            # Update costliest price, if current price is higher and within budget
            if (price > costliestPrice) and (price <= maxPrice):
                # Update price of costliest configuration
                costliestPrice = price
                # Save configuration
                costliestTrim = trim
                costliestExtra = extra_indicator	   

    # Generate specification
    carSpecification = ", ".join(np.append(TrimString[costliestTrim], ExtraString[costliestExtra]))

    return carSpecification


            
            
    
        
            
            