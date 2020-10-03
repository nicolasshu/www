---
layout: article
title: "How to Heat your room with Hot Water"
tags:
  - Chemistry & Biochemistry
  - Instructions
permalink: heat_room_with_water.html
---

Many of us may potentially go through some rough patches and need to resort oneself to different resources in order to fight the cold during harsh winters. What one may find is that hot water can be potentially a cheap resource to heat up your room/apartment

| Temperature ($$^oC$$) | Heat Capacity ($$J/(mol \cdot K)$$) | Heat Capacity ($$J/(g \cdot K)$$)  |
| :------------: |:-------------:| :-----:|
|   0 | 75.97 | 4.2176 |
|  10 | 75.42 | 4.1921 |
|  25 | 75.33 | 4.1818 |
|  20 | 75.28 | 4.1814 |
|  30 | 75.26 | 4.1784 |
|  40 | 75.26 | 4.1785 |
|  50 | 75.30 | 4.1806 |
|  60 | 75.37 | 4.1843 |
|  70 | 75.46 | 4.1895 |
|  80 | 75.58 | 4.1963 |
|  90 | 75.74 | 4.2050 |
| 100 | 75.94 | 4.2159 |

So, in general, we'll say that the heat capacity of water, assuming constant pressure is

$$C_{p,H_2O}^o = 75 \frac{J}{mol \cdot K}$$

*In this case, we'll initially utilize only variables and in the end we will plug in values.*

So we have an apartment (with no walls) with volume $$V_{apt}$$ (in liters). Our condition has an initial temperature $$T_i$$, and we with to bring up the temperature to $$T_f$$. Thus we can say

$$\Delta T = T_f - T_i$$

In our case, we can or cannot utilize ideal gas laws to estimate the volumes of a mole of gas. Clayperon provided the ideal gas law, which was a combinations of contributions of Charles's law ($$\frac{V}{T} = k$$), Boyle's law ($$PV = k$$), Avogadro's law ($$\frac{V}{n} = k$$), and Gay-Lussac's law ($$\frac{P}{T} = k$$), where $$P$$ is pressure, $$V$$ is volume, $$n$$ is the number of moles, $$T$$ is the temperature in Kelvin, and we will use the gas constant $$R$$.

$$PV = nRT$$

$$\frac{V}{n} = \frac{RT}{P}$$

In this case, $$T$$ would be a dynamic variable, in which would change the volume that a mole of gas would occupy at that initial temperature $$T_i$$.

$$\frac{V}{n} = \frac{RT}{P} = \frac{0.08206 \frac{L \cdot atm}{mol \cdot K }\cdot T_i K }{1 atm}$$

So we can say that the amout of heat needed to warm up the air would be

$$q_{air} = n_{air} C_{p,air}^o \Delta T$$

$$q_{air} = \left( \frac{V_{apt}}{V/n} \right) C_{p,air}^o \Delta T$$

$$q_{air} = \left( \frac{V_{apt}}{\frac{RT_i}{P}} \right) C_{p,air}^o (T_f-T_i)$$

And we know that, when thinking in ideal gases,

$$C_{p,air}^o = \frac{5}{2}R \quad \text{(monoatomic gases)}$$

$$C_{p,air}^o = \frac{7}{2}R \quad \text{(diatomic gases)}$$

$$C_{p,air}^o = 4R \quad \text{(polyatomic gases)}$$

But since we have about 70% $$N_2$$, then we have a lot of $$O_2$$, some $$H_2$$, we'll assume that we have as a majority, diatomic gases. Therefore

$$q_{air} = \left( \frac{V_{apt}}{\frac{RT_i}{P}} \right) \frac{7R}{2} (T_f-T_i)$$

So $$q_{air}$$ will the the amount of energy that will be needed to warm up the air from $$T_i$$ to $$T_f$$. This means that this will be the amount of heat needed to be released from water in order to cool the water, making it into an exothermic process (not reaction*).

$$-q_{air} = n_{H_2O} C_{p,H_2O}^o \Delta T_{H_2O}$$

$$-q_{air} = n_{H_2O} C_{p,H_2O}^o \Delta T_{H_2O}$$

Then you simply need to solve for $$n_{H_2O}$$ and convert it to liters. Note that the final temperature of the water will be equalized with the temperature of the room

$$n_{H_2O} = -\frac{q_{air}}{C_{p,H_2O}^o \Delta T_{H_2O}}$$

$$n_{H_2O} = -\frac{\left( \frac{V_{apt}}{\frac{RT_{i,apt}}{P}} \right) \frac{7R}{2} (T_f-T_{i,apt})}{C_{p,H_2O}^o (T_f - T_{i,H_2O})}$$

$$n_{H_2O} = -\frac{ 7V_{apt}P(T_f-T_{i,apt})}{2T_{i,apt} C_{p,H_2O}^o (T_f - T_{i,H_2O})}$$

Note that units really do matter, so temperatures have to be in Kelvin, volumes have to be in either liters or $$dm^3$$, our heat capacities are better to be in $$\frac{J}{mol \cdot K}$$, and pressure has to be in Pascals, so at sea level, $$P = 101325 \text{Pa}$$.

Just to be sure,

| Variable | What is it? |
| :------------: |:-------------:|
| $$V_{apt}$$ | Volume of the apartment |
| $$P$$ | Atmospheric pressure |
| $$T_f$$ | Final desired temperature (of water and apartment) |
| $$T_{i,apt}$$ | Initial temperature of the apartment |
| $$T_{i,H_2O}$$| Initial temperature of the water |
| $$C_{p,H_2O}^o$$ | Heat capacity of water |

Finally, to compute the amount of water needed, the molecular mass of water is 18 g, and the density of water is 1g/ml, thus,

$$V_{H_2O} = n_{H_2O} \cdot \frac{18 g H_2O}{mol H_2O} \cdot \frac{1 ml H_2O}{g H_2O}$$

$$V_{H_2O} = -\frac{ 7V_{apt}P(T_f-T_{i,apt})}{2T_{i,apt} C_{p,H_2O}^o (T_f - T_{i,H_2O})} \cdot \frac{18 ml H_2O}{mol H_2O} $$

## Example

Let say that the volume of your apartment is $$V_{apt}=30000 L$$, you live at sea level ($$P=101325 \text{ Pa} = 101.325 \text{ kPa}$$), your apartment is currently at 3 $$^oC$$ ($$T_{i,apt} = 276 K$$), you are planning on boiling water ($$T_{i,H_2O} = 373 K$$), we assume that the heat capacity of water is 75 $$\frac{J}{mol \cdot K}$$, and you wish your apartment to be at room temperature 25 $$^oC$$ ($$T_f = 298 K$$), then

This would yield about 150.7 moles of water at 100 $$^oC$$ needed, which in turns, requires 2.714 L of boiling water to warm up your 30 kL apartment.
