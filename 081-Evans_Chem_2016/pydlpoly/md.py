import pydlpoly

pd = pydlpoly.pydlpoly("dut49")
# enforce triclinic -> otherwise all is orthorombic
pd.setup(bcond=3)

# do a first round of NVT with a quick/fast Berendsen Thermostat
pd.MD_init("equil_NVT", T=300.0, p=0.001, startup=True, ensemble="nvt", thermo="ber", relax=(0.1,))
pd.MD_run(20000)



# now start up NsT with a Hoover thermostat .. first for equlibrating
pd.MD_init("equil_NPT", T=300.0, p=0.001, ensemble="npt", thermo="hoover", relax=(1.0, 2.0))
pd.MD_run(1000000)



# finally sample NsT with a Hoover thermostat
pd.MD_init("sample_NPT", T=300.0, p=0.001, ensemble="npt", thermo="hoover", relax=(1.0, 2.0), traj=["cell", "xyz"], tnstep=10)
pd.MD_run(5000000)
