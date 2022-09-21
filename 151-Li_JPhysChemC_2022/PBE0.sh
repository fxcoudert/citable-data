@SET SYSNAME  40Na2O-60CaO-300SiO2-33CdSe-20ps 
@SET CELL 25.112

&GLOBAL
    PRINT_LEVEL MEDIUM
    PROJECT_NAME ${SYSNAME}
    RUN_TYPE Energy
&END GLOBAL

&FORCE_EVAL
    METHOD  QS
    STRESS_TENSOR  DIAGONAL_ANALYTICAL
    &DFT
        BASIS_SET_FILE_NAME HFX_BASIS
        BASIS_SET_FILE_NAME BASIS_MOLOPT
        BASIS_SET_FILE_NAME BASIS_ADMM
        BASiS_SET_FILE_NAME BASIS_ADMM_MOLOPT
        POTENTIAL_FILE_NAME GTH_POTENTIALS
        WFN_RESTART_FILE_NAME ./40Na2O-60CaO-300SiO2-33CdSe-20ps-pbe0-RESTART.wfn
        &POISSON
            PERIODIC XYZ
        &END POISSON
        &SCF
            MAX_SCF    200
            EPS_SCF    1.0e-5
            SCF_GUESS  RESTART 
            &MIXING  T
                METHOD   PULAY_MIXING
                ALPHA    0.5
                NBUFFER  5
            &END MIXING
            &PRINT
                &RESTART ON
                &END RESTART
            &END PRINT
            &OT ON
                PRECONDITIONER  FULL_SINGLE_INVERSE
                MINIMIZER       DIIS
            &END OT
        &END SCF
        &QS
            METHOD  GPW
            EPS_DEFAULT     1e-10
            EPS_PGF_ORB     1e-30
            EPS_FILTER_MATRIX    0
        &END QS
        &MGRID
            NGRIDS 4
            CUTOFF 600        #The cutoff of the finest grid level
            REL_CUTOFF 40     #Determines the grid at which a Gaussian is mapped, giving the cutoff used for a gaussian with alpha=1 
        &END MGRID
        &XC
            &XC_FUNCTIONAL 
                &PBE 
                    SCALE_X   0.75 #75% GGA exchange
                    SCALE_C   1.0  #100% GGA correlation
                &END PBE 
                &PBE_HOLE_T_C_LR
                    CUTOFF_RADIUS 4.0
                    SCALE_X       0.25
                &END PBE_HOLE_T_C_LR
            &END XC_FUNCTIONAL
            &HF 
                FRACTION  0.25
                &SCREENING
                    EPS_SCHWARZ 1e-6
                    SCREEN_ON_INITIAL_P TRUE
                &END SCREENING
                &INTERACTION_POTENTIAL
                    POTENTIAL_TYPE  TRUNCATED
                    CUTOFF_RADIUS   2.0
                    T_C_G_DATA   t_c_g.dat
                &END INTERACTION_POTENTIAL
            &END HF 
            DENSITY_CUTOFF      1e-10  #The cutoff on the density used by the xc calculation
            GRADIENT_CUTOFF     1e-10  #The cutoff on the gradient density of density used by xc calculation
            TAU_CUTOFF          1e-10  #The cutoff on tau used by the xc  calculation
            &VDW_POTENTIAL
                POTENTIAL_TYPE  PAIR_POTENTIAL
                &PAIR_POTENTIAL
                    R_CUTOFF    9     #Range of potential. The cutoff will be 2 times of this value
                    TYPE        DFTD3
                    PARAMETER_FILE_NAME /public/home/users/whut005/cp2k-6.1.0/data/dftd3.dat
                    REFERENCE_FUNCTIONAL PBE0
                    LONG_RANGE_CORRECTION T
                &END PAIR_POTENTIAL
            &END VDW_POTENTIAL
        &END XC
        &AUXILIARY_DENSITY_MATRIX_METHOD
            ADMM_PURIFICATION_METHOD   MO_DIAG
            METHOD   BASIS_PROJECTION
        &END AUXILIARY_DENSITY_MATRIX_METHOD            
        &PRINT
            &PDOS
                NLUMO -1
                COMPONENTS
            &END PDOS
            &MO_CUBES
                NHOMO  5
                NLUMO  5
            &END MO_CUBES    
        &END PRINT
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
            BASIS_SET AUX_FIT cFIT11
            POTENTIAL GTH-PBE-q12
        &END KIND
        &KIND Se
            BASIS_SET DZVP-MOLOPT-SR-GTH
            BASIS_SET AUX_FIT cFIT6
            POTENTIAL GTH-PBE-q6
        &END KIND
        &KIND Na
            BASIS_SET DZVP-MOLOPT-SR-GTH
            BASIS_SET AUX_FIT cFIT3
            POTENTIAL GTH-PBE-q9
        &END KIND
        &KIND O
            BASIS_SET DZVP-MOLOPT-GTH
            BASIS_SET AUX_FIT cFIT3
            POTENTIAL GTH-PBE-q6
        &END KIND
        &KIND Si
            BASIS_SET DZVP-MOLOPT-GTH
            BASIS_SET AUX_FIT cFIT3
            POTENTIAL GTH-PBE-q4
        &END KIND
        &KIND Ca
            BASIS_SET DZVP-MOLOPT-SR-GTH
            BASIS_SET AUX_FIT cFIT11
            POTENTIAL GTH-PBE-q10
        &END KIND
    &END SUBSYS
&END FORCE_EVAL
