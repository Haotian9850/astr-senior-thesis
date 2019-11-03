#!/usr/bin/env casarun
import admit


num_sigma = 1
min_chan = 2
max_chan = 10
fits_file_name = "/mnt/documents-local/ASTR4998/astr-senior-thesis/workspace/statcont_admit_pipeline/products/SerpS_TC_spw2.pbcor_cutout_180_180_100_line.fits"
vlsr = 8.0


if __name__ == "__main__":
    p = admit.Project(fits_file_name + ".admit", dataserver=True) 
    t0  = p.addtask(admit.Ingest_AT(file=fits_file_name))
    t1  = p.addtask(admit.CubeStats_AT(ppp=True), [t0])
    t2  = p.addtask(admit.Moment_AT(mom0clip=2.0, numsigma=[num_sigma]), [t0, t1])
    t3  = p.addtask(admit.CubeSpectrum_AT(), [t0, t2])
    t4 = p.addtask(admit.LineID_AT(
        tier1width = 10,
        vlsr = 8.0,
        numsigma = num_sigma,
        minchan = min_chan,
        maxgap = max_chan, 
        identifylines = True,
        allowexotics = True,
        recomblevel = "deep",
    ), [t1, t3])
    p.run()
