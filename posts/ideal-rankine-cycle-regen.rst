Ideal Rankine Cycle with feedwater heater calculations
======================================================

.. post:: May 5, 2020
   :exclude:
   :tags: tutorial, thermodynamics, rankine-cycle, PYroMat
   :author: adriaan

How to calculate the thernal efficiency of an Ideal Rankine Cycle with feedwater heaters using Python and PYroMat

The problem
-----------

Consider a regenerative cycle using steam as the working fluid. 
Steam leaves the boiler and enters the turbine at 4 MPa, :math:`\text{400}^\circ\text{C}`. 
After expansion to 400 kPa, some of the steam is extracted from the turbine to heat the feedwater in an open FWH. 
The pressure in the FWH is 400 kPa, and the water leaving it is saturated liquid at 400 kPa. 
The steam not extracted expands to 10 kPa. Determine the cycle efficiency.

.. figure:: /images/ideal-rankine-cycle-regen-problem-image.png
   :width: 80%

Looking at the mass flow of steam entering and exiting the turbine:

.. math::

    y = \dot{m}_6/\dot{m}_5

and thus $\dot{m}_6$ can be written as a function of :math:`\dot{m}_5`:

.. math::

    \dot{m}_6 = y\dot{m}_5

Similarly :math:`\dot{m}_7` can be written as:

.. math::

    \dot{m}_7=(1-y)\dot{m}_5

and 

.. math::

    \dot{m}_7=(1-y)\dot{m}_5=\dot{m}_1=\dot{m}_2

Initiate PYroMat 
----------------

.. code-block:: python

    import pyromat as pm
    import numpy as np

    pm.config["unit_pressure"] = "kPa"
    pm.config["def_p"] = 100

    mp_water = pm.get("mp.H2O") # <-- for multi-phase water properties

To solve this problem we consider a control surface around the pump, the boiler, the turbine, and the condenser.

The low pressure pump
---------------------

First, let us consider the **low pressure pump**:

.. code-block:: python

    p1 = 10 # <-- given
    p2 = 400 # <-- given

    v1 = 1/mp_water.ds(p=p1)[0]

    w_pump1 = v1*(p2-p1)
    h2 = h1+w_pump1
    print(f"Work required by pump 1: {round(float(w_pump1),1)} kJ/kg")

.. code-block:: bash

    Work required by pump 1: 0.4 kJ/kg

The turbine
-----------

Next, let's consider **the turbine**:

.. code-block:: python

    p5 = 4000 # <-- given
    T5 = 400+273.15 # K <-- given
    h5 = mp_water.h(p=p5, T=T5)
    s5 = mp_water.s(p=p5, T=T5)

    s6 =s5
    p6 = 400 # <-- given
    T6, x6 = mp_water.T_s(s=s6, p=p6, quality=True)
    h6 = mp_water.h(x=x6, p=p6)

    print(f"Quality of bled steam: {round(float(x6),4)}")

.. code-block:: bash

    Quality of bled steam: 0.9757
    
The feedwater heater
--------------------

Now, let's consider the **feedwater heater**:

.. code-block:: python

    p3 = 400 # <-- given
    h3 = mp_water.hs(p=p3)[0]

The energy conservation equation for the FWH is: 

.. math::
    
    y(h_6)+(1-y)h_2 = h_3

This can be re-arranged to solve :math:`y` explicitly: 

.. math::
    
    y = \frac{h_2 - h_3}{h_2 - h_6}

.. code-block:: python

    y = (h2-h3)/(h2-h6)
    print(f"y = {round(float(y),4)}")

.. code-block:: bash

    y = 0.1654
   
Work done by turbine
--------------------

We can now calculate the work extracted by the turbine:

.. code-block:: python

    p7 = p1
    s7 = s5
    T7, x7 = mp_water.T_s(s=s7, p=p7, quality=True)
    h7 = mp_water.h(x=x7, p=p7)
    w_t = h5 - y*h6 - (1-y)*h7
    print(f"Work generated by turbine: {round(float(w_t),1)} kJ/kg")

.. code-block:: bash

    Work generated by turbine: 980.4 kJ/kg

The high pressure pump
----------------------

Next, let's consider the high pressure pump:

.. code-block:: python

    p4 = 4000 # <-- given
    v3 = 1/mp_water.ds(p=p3)[0]
    w_pump2 = v3*(p4-p3)
    print(f"Work required by pump 2: {round(float(w_pump2),1)} kJ/kg")

.. code-block:: bash

    Work required by pump 2: 3.9 kJ/kg
   
The boiler
----------

Finally, we can consider the **boiler**:

.. code-block:: python

    h4 = h3 + w_pump2
    q_H = h5-h4
    print(f"Heat input by boiler: {round(float(q_H),1)} kJ/kg")

.. code-block:: bash

    Heat input by boiler: 2605.9 kJ/kg

Thermal efficiency
------------------
   
We can now calculate the thermal efficiency with 

.. math::
    
    \eta_{th}=\frac{w_{net}}{q_H}

.. code-block:: python

    eta_th = (w_t - w_pump1*(1-y) - w_pump2)/q_H*100
    print(f"Thermal efficiency is: {round(float(eta_th),2)}%")

.. code-block:: bash

    Thermal efficiency is: 37.46%


