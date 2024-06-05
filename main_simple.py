#!/usr/bin/env python
# coding: utf-8

# # ViperGPT -- Quick Start
# 
# This notebook is meant to be a quick entry into ViperGPT. **Warning:** This notebook will execute arbitrary code on your machine. Proceed at your own risk.
# 
# Before running this code, modify any parameters at `configs/my_config.yaml`. For example, you may want to change the BLIP model (`blip_v2_model_type`) from XXL to XL if your GPU does not have enough memory.

# In[1]:


from main_simple_lib import *


# In[2]:


im = load_image('https://viper.cs.columbia.edu/static/images/kids_muffins.jpg')
query = 'How many muffins can each kid have for it to be fair?'

show_single_image(im)
code = get_code(query)


# In[3]:


execute_code(code, im, show_intermediate_steps=True)

