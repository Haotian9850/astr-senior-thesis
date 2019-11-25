#!/usr/bin/env casarun
# set up admit in the casa environment
import admit
# define project name
p = admit.Project('test.admit',dataserver=True )
# Flow tasks.
t0  = p.addtask(admit.Ingest_AT(file="/media/haotian/documents-local/ASTR4998/data/data/SerpS_TC_spw0.pbcor.fits"))
t1  = p.addtask(admit.CubeStats_AT(ppp=True), [t0])
t2  = p.addtask(admit.Moment_AT(mom0clip=2.0, numsigma=[3.0]), [t0, t1])
t3  = p.addtask(admit.CubeSpectrum_AT(), [t0, (t2,0)])
p.run()