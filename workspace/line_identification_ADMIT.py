#!/usr/bin/env casarun
import admit


NUM_SIGMA = 2
MIN_CHAN = 2
MAX_CHAN = 20
FITS_CUBE = "/media/haotian/documents-local/ASTR4998/data/products/SerpS_TC_spw2.pbcor_cutout_180_180_100_line.fits"
VLSR = 8.0


if __name__ == "__main__":
    p = admit.Project(
        "{}.admit_BDP".format(FITS_CUBE),
        dataserver=True
    )
    t0 = p.addtask(admit.Ingest_AT(file=FITS_CUBE))
    t1 = p.addtask(admit.CubeStats_AT(ppp=True), [t0])
    t2 = p.addtask(admit.Moment_AT(mom0clip=2.0, numsigma=[NUM_SIGMA]), [t0, t1])
    t3 = p.addtask(admit.CubeSpectrum_AT(), [t0, t2])
    t5 = p.addtask(admit.LineSegment_AT(maxgap=MAX_CHAN, minchan=MIN_CHAN, numsigma=NUM_SIGMA, csub=[0,0]), [t1, t3])
    t6 = p.addtask(admit.ContinuumSub_AT(), [t0, t5])
    t7 = p.addtask(admit.CubeStats_AT(ppp=True), [t6])
    t8 = p.addtask(admit.Moment_AT(mom0clip=2.0, numsigma=[NUM_SIGMA]), [t6, t7])
    t9 = p.addtask(admit.CubeSpectrum_AT(), [t6, t8])
    t10 = p.addtask(admit.LineID_AT(allowexotics=True, maxgap=MAX_CHAN, minchan=MIN_CHAN, numsigma=NUM_SIGMA, recomblevel='deep', tier1width=10.0, vlsr=VLSR, csub=[0,None]), [t7, t9])
    t11 = p.addtask(admit.LineCube_AT(), [t6, t10])
    t12 = p.addtask(admit.Moment_AT(mom0clip=2.0, moments=[0, 1, 2]), [t11, t7])
    t13 = p.addtask(admit.CubeSpectrum_AT(), [t11, t12])
    
    p.run()

