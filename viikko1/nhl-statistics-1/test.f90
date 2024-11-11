program cosh_vertailu
        implicit none
        real :: x, manual_cosh, fortran_cosh

        do i = 0, 10,1  
                manual_cosh = (exp(x)+exp(-x))/2.0
                fortran_cosh = cosh(x)
                relative_difference = abs(manual_cosh - fortran_cosh) / abs(fortran_cosh)

                





