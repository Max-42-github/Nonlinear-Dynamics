#### Lorenz Attractor

<center>
    <i>
        "If this intellect were vast enough to submit the data to analysis... then the future, just like the past would be present before its eyes." 
    </i>
    - P.S Laplace
</center>

![lorenz](https://github.com/user-attachments/assets/a9f903b4-3773-4934-96f9-4e25548086bb)

The above diagram shows the phase trajectory (x,y,z) for system of diffrential equations called the Lorenz System. The Lorenz system is described by the following set of equaitons : 

$$
\frac{dx}{dt} = \sigma (y-x) 
$$

$$
\frac{dy}{dt} = x(\rho - z) - y
$$

$$
\frac{dz}{dt} = xt - \beta z
$$

Famous set of parameters, as choosen by Lorenz are $\sigma = 10$, $\beta = 8/3$ and $\rho = 28$.
This system is one of the earliest example of chaotic system and to express the Sensitive Dependence on Initial Condition (SDIC). Although the system is chaotic in nature but, on observing the phase trajectories over some period of time the random trajectories seems to be confined within a certain region. The system seems to be attracted towards two points in a shape like 'Butterfly'. 

The goal of this program is to observe this attracting nature of the phase trajectories of the Lorentz System. And to also obverve two very close initial points evolving to two very different trajectories with time; showing the SDIC of the system.
