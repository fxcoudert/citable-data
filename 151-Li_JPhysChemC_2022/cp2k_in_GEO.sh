@SET SYSNAME 40Na2O-60Ca-300SiO2-33CdSe
@SET CELL   25.112

&GLOBAL
    PRINT_LEVEL MEDIUM
    PROJECT_NAME ${SYSNAME}
    Run_TYPE GEO_OPT
&END GLOBAL

&FORCE_EVAL
    METHOD  QS
    STRESS_TENSOR  DIAGONAL_ANALYTICAL
    &DFT
        BASIS_SET_FILE_NAME BASIS_SET
        BASIS_SET_FILE_NAME BASIS_MOLOPT
        POTENTIAL_FILE_NAME POTENTIAL
        &SCF
            MAX_SCF    200
            EPS_SCF    1.0e-5
            SCF_GUESS  ATOMIC
            &MIXING  T
                METHOD   PULAY_MIXING
                ALPHA    0.5
                NBUFFER  5
            &END MIXING
            &PRINT
                &RESTART OFF
                &END RESTART
            &END PRINT
            &OT ON
                PRECONDITIONER  FULL_SINGLE_INVERSE
                MINIMIZER       DIIS
            &END OT
        &END SCF
        &QS
            EPS_DEFAULT     1e-10
        &END QS
        &MGRID
            NGRIDS 4
            CUTOFF 600        #The cutoff of the finest grid level
            REL_CUTOFF 40     #Determines the grid at which a Gaussian is mapped, giving the cutoff used for a gaussian with alpha=1 
        &END MGRID
        &XC
            &XC_FUNCTIONAL PBE
            &END XC_FUNCTIONAL
            DENSITY_CUTOFF      1e-10  #The cutoff on the density used by the xc calculation
            GRADIENT_CUTOFF     1e-10  #The cutoff on the gradient density of density used by xc calculation
            TAU_CUTOFF          1e-10  #The cutoff on tau used by the xc  calculation
            &VDW_POTENTIAL
                POTENTIAL_TYPE  PAIR_POTENTIAL
                &PAIR_POTENTIAL
                    R_CUTOFF    9     #Range of potential. The cutoff will be 2 times of this value
                    TYPE        DFTD3
                    PARAMETER_FILE_NAME dftd3.dat
                    REFERENCE_FUNCTIONAL PBE
                    LONG_RANGE_CORRECTION T
                &END PAIR_POTENTIAL
            &END VDW_POTENTIAL
        &END XC
    &END DFT
    &SUBSYS
        &TOPOLOGY
            COORD_FILE ${SYSNAME}.xyz
            COORD_FILE_FORMAT XYZ
            CONN_FILE_FORMAT OFF
        &END TOPOLOGY
        &CELL
            ABC ${CELL} ${CELL} ${CELL}
            ALPHA_BETA_GAMMA 90.0 90.0 90.0
            MULTIPLE_UNIT_CELL  1 1 1
            PERIODIC XYZ
        &END CELL
        &KIND Cd
            BASIS_SET DZVP-MOLOPT-SR-GTH
            POTENTIAL GTH-PBE-q12
        &END KIND
        &KIND Se
            BASIS_SET DZVP-MOLOPT-SR-GTH
            POTENTIAL GTH-PBE-q6
        &END KIND
        &KIND Na
            BASIS_SET DZVP-MOLOPT-SR-GTH
            POTENTIAL GTH-PBE-q9
        &END KIND
        &KIND O
            BASIS_SET DZVP-MOLOPT-GTH
            POTENTIAL GTH-PBE-q6
        &END KIND
        &KIND Si
            BASIS_SET DZVP-MOLOPT-GTH
            POTENTIAL GTH-PBE-q4
        &END KIND
        &KIND Ca
            BASIS_SET DZVP-MOLOPT-SR-GTH
            POTENTIAL GTH-PBE-q10
        &END KIND
    &END SUBSYS
&END FORCE_EVAL
# For energy minimization
&MOTION
    &GEO_OPT
        TYPE MINIMIZATION
        MAX_ITER 200
        OPTIMIZER CG
    &END GEO_OPT
    &PRINT
        &RESTART
            FILENAME =${SYSNAME}.min.rst
            &EACH
                GEO_OPT 1
            &END EACH
        &END RESTART
    &END PRINT
&END MOTION


