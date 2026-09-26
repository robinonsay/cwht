#!/bin/sh
# Emulation scenario runner (07 section 1.2 Scripts row; gate step G6 of 07 section 8.4).
# FW-B0 stub: no emulator is accepted until the PDR emulator ADR (ADR-011 section 3), so the
# runner prints the SKIP line and exits 0 without running any scenario. It is completed once
# that ADR is Accepted. Arguments (--all, --report PATH) are accepted and ignored.
echo "SKIP emulation: no accepted emulator ADR"
exit 0
