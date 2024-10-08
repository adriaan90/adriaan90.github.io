Create a fuel file in Ricardo WAVE
==================================

.. post:: December 29, 2020
  :exclude:
  :author: adriaan
  :tags: how-to, Ricardo-WAVE

How to create a fuel file in Ricardo WAVE.

The following instructions can be used to create a fuel file for Ricardo WAVE. 
You can use this to either create a .fue file consisting of one blend component, or a blend with more than one:

1. Ensure you have downloaded the .dat files of the fuels you want to blend.
2. Open up the command prompt window (Start button->Search->"cmd"-> click on cmd.exe)
3. Ensure the command prompt is opened in the folder where the .dat files are saved. To change to the correct folder path:

   1. Copy the file path in your Windows Explorer window. First open the folder where the files are.
   2. Click on the little folder icon on the left of the file path and copy the file path.
   3. Use command `cd` followed by the file path and press enter.
   4. The new line in the command prompt will now show that it is open in the folder where the .dat files are.

4. Now enter the following command:

.. code-block:: bash   

    buildfuel -d diesel.dat ethanol.dat FAME.dat -f 0.89 0.09 0.02 -p Blended_Fuel

The above command is to create a B2E9 blend. 
First the .dat files of all the fuels that will be used in the blend are listed, then the percentage of each fuel in the blend and then the name you want to call the fuel file. 
For binary blends the command line will be:

.. code-block:: bash

    buildfuel -d diesel.dat ethanol.dat -f 0.80 0.20 -p E20
    
The above command is to create a binary blend of E20 blend.

