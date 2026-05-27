# Host Header Verification Report

## Metadata

- Tool: `Host Header Research Tool`
- Version: `2.0`
- Run date: `2026-05-26T19:54:06.564919+00:00`
- Fake Host header: `attacker.com`
- Total tests: `1350`
- Schemes: `https, http`

## Summary

| Classification | Count | Percentage |
|---|---:|---:|
| Different content with same status | 20 | 1.48% |
| Different response | 42 | 3.11% |
| Inconclusive | 57 | 4.22% |
| Possible Host header injection | 31 | 2.3% |
| Redirects invalid Host | 61 | 4.52% |
| Safe / strict Host validation | 1112 | 82.37% |
| Weak Host validation | 27 | 2.0% |

## Interpretation guide

| Classification | Meaning |
|---|---|
| Safe / strict Host validation | Invalid Host was rejected or blocked. |
| Weak Host validation | Same/similar content returned for arbitrary Host. This is a weak validation signal, not proof of exploitability. |
| Possible Host header injection | Injected Host appeared in Location, Set-Cookie, or security-relevant application output. Manual verification required. |
| Redirects invalid Host | Invalid Host caused redirect, but not to the injected Host. Usually safe if canonical. |
| Different response | The server behaved differently; no clear arbitrary Host acceptance. |
| Inconclusive | Network, timeout, or baseline failure. |

## Detailed results

| Target | Scheme | Baseline | Invalid Host | Similarity | Reflection | Server-footer only | Classification | Risk |
|---|---|---:|---:|---:|---|---|---|---|
| `kv.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `kv.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `cert.ee` | `https` | 301 | 403 | 0.3414 | No | False | Safe / strict Host validation | Low |
| `cert.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `icds.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `icds.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `arvutitark.ee` | `https` | 200 | 403 | 0.0383 | No | False | Safe / strict Host validation | Low |
| `arvutitark.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `hm.ee` | `https` | 200 | 403 | 0.031 | No | False | Safe / strict Host validation | Low |
| `hm.ee` | `http` | 301 | 403 | 0.0117 | No | False | Safe / strict Host validation | Low |
| `piksel.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `piksel.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `membershop.ee` | `https` | 200 | 403 | 0.0269 | No | False | Safe / strict Host validation | Low |
| `membershop.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `viinarannasta.ee` | `https` | 200 | 421 | 0.0122 | No | False | Safe / strict Host validation | Low |
| `viinarannasta.ee` | `http` | 301 | 403 | 0.0337 | No | False | Safe / strict Host validation | Low |
| `f48.ee` | `https` | 200 | 200 | 0.0269 | No | False | Different content with same status | Low/Medium |
| `f48.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `ut.ee` | `https` | 301 | 403 | 0.2203 | No | False | Safe / strict Host validation | Low |
| `ut.ee` | `http` | 301 | 403 | 0.0271 | No | False | Safe / strict Host validation | Low |
| `astravelo.ee` | `https` | 200 | 403 | 0.0326 | No | False | Safe / strict Host validation | Low |
| `astravelo.ee` | `http` | 301 | 403 | 0.0456 | No | False | Safe / strict Host validation | Low |
| `1a.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `1a.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `maksekeskus.ee` | `https` | 200 | 403 | 0.0058 | No | False | Safe / strict Host validation | Low |
| `maksekeskus.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `ester.ee` | `https` | 301 | 421 | 0.2842 | No | False | Safe / strict Host validation | Low |
| `ester.ee` | `http` | 301 | 403 | 0.0139 | No | False | Safe / strict Host validation | Low |
| `online-casino.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `online-casino.ee` | `http` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `poki.ee` | `https` | 200 | 403 | 0.0376 | No | False | Safe / strict Host validation | Low |
| `poki.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `weby.ee` | `https` | 200 | 200 | 0.9818 | No | False | Weak Host validation | Medium |
| `weby.ee` | `http` | 301 | 403 | 0.0439 | No | False | Safe / strict Host validation | Low |
| `handymann.ee` | `https` | 200 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `handymann.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `auto24.ee` | `https` | 302 | 403 | 0.5245 | No | False | Safe / strict Host validation | Low |
| `auto24.ee` | `http` | 301 | 403 | 0.0144 | No | False | Safe / strict Host validation | Low |
| `ssb.ee` | `https` | 200 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `ssb.ee` | `http` | 301 | 403 | 0.0129 | No | False | Safe / strict Host validation | Low |
| `soccernet.ee` | `https` | 200 | 403 | 0.0289 | No | False | Safe / strict Host validation | Low |
| `soccernet.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `autmo.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `autmo.ee` | `http` | 301 | 403 | 0.0421 | No | False | Safe / strict Host validation | Low |
| `utlib.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `utlib.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `ml.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `ml.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `kika.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `kika.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `alfanet.ee` | `https` | 200 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `alfanet.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `litres.ee` | `https` | 301 | 302 | 0.1043 | Cookie, Headers | False | Possible Host header injection | High |
| `litres.ee` | `http` | 301 | 403 | 0.0481 | No | False | Safe / strict Host validation | Low |
| `tr.ee` | `https` | 200 | 421 | 0.0019 | No | False | Safe / strict Host validation | Low |
| `tr.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `yandex.ee` | `https` | 302 | 406 | 1.0 | Cookie, Headers | False | Possible Host header injection | High |
| `yandex.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `heateenindus.ee` | `https` | 200 | 421 | 0.0089 | No | False | Safe / strict Host validation | Low |
| `heateenindus.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `oci.ee` | `https` | 200 | 403 | 0.0446 | No | False | Safe / strict Host validation | Low |
| `oci.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `le.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `le.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `roba.ee` | `https` | 200 | 403 | 0.031 | No | False | Safe / strict Host validation | Low |
| `roba.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `kalevspa.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `kalevspa.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `tireman.ee` | `https` | 200 | 421 | 0.0044 | No | True | Safe / strict Host validation | Low |
| `tireman.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `osta.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `osta.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `kokkama.ee` | `https` | 301 | 404 | 0.032 | No | False | Safe / strict Host validation | Low |
| `kokkama.ee` | `http` | 301 | 403 | 0.0135 | No | False | Safe / strict Host validation | Low |
| `whs.ee` | `https` | 200 | 400 | 0.0166 | No | True | Safe / strict Host validation | Low |
| `whs.ee` | `http` | 200 | 403 | 0.0479 | No | False | Safe / strict Host validation | Low |
| `solnet.ee` | `https` | 200 | 421 | 0.0107 | No | False | Safe / strict Host validation | Low |
| `solnet.ee` | `http` | 301 | 403 | 0.0129 | No | False | Safe / strict Host validation | Low |
| `tt.ee` | `https` | 200 | 400 | 0.0592 | No | True | Safe / strict Host validation | Low |
| `tt.ee` | `http` | 301 | 403 | 0.0421 | No | False | Safe / strict Host validation | Low |
| `muis.ee` | `https` | 301 | 400 | 0.3407 | No | False | Safe / strict Host validation | Low |
| `muis.ee` | `http` | 302 | 403 | 0.014 | No | False | Safe / strict Host validation | Low |
| `cyber.ee` | `https` | 200 | 302 | 0.0109 | No | True | Redirects invalid Host | Low |
| `cyber.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `riigitootaja.ee` | `https` | 301 | 400 | 0.0 | No | False | Safe / strict Host validation | Low |
| `riigitootaja.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `pokerstars.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `pokerstars.ee` | `http` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `maarahvapood.ee` | `https` | 200 | 421 | 0.0091 | No | True | Safe / strict Host validation | Low |
| `maarahvapood.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `orb.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `orb.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `domeeninimi.ee` | `https` | 200 | 403 | 0.0253 | No | False | Safe / strict Host validation | Low |
| `domeeninimi.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `autodoc.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `autodoc.ee` | `http` | 308 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `sirp.ee` | `https` | 301 | 302 | 0.0 | Location, Headers | False | Possible Host header injection | High |
| `sirp.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `bauhof.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `bauhof.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `goldtime.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `goldtime.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `terviseamet.ee` | `https` | 200 | 403 | 0.0291 | No | False | Safe / strict Host validation | Low |
| `terviseamet.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `tallinn-airport.ee` | `https` | 301 | 421 | 0.3912 | No | True | Safe / strict Host validation | Low |
| `tallinn-airport.ee` | `http` | 301 | 403 | 0.014 | No | False | Safe / strict Host validation | Low |
| `jallacasino.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `jallacasino.ee` | `http` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `bmw.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `bmw.ee` | `http` | 200 | 403 | 0.0211 | No | False | Safe / strict Host validation | Low |
| `hhkungfu.ee` | `https` | 200 | 403 | 0.0268 | No | False | Safe / strict Host validation | Low |
| `hhkungfu.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `digar.ee` | `https` | 302 | 302 | 0.9541 | No | True | Redirects invalid Host | Low |
| `digar.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `poff.ee` | `https` | 200 | 200 | 0.0198 | No | False | Different content with same status | Low/Medium |
| `poff.ee` | `http` | 302 | 403 | 0.0355 | No | False | Safe / strict Host validation | Low |
| `ubuy.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `ubuy.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `kliinikum.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `kliinikum.ee` | `http` | 301 | 403 | 0.0214 | No | False | Safe / strict Host validation | Low |
| `zxart.ee` | `https` | 200 | 421 | 0.0133 | No | True | Safe / strict Host validation | Low |
| `zxart.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `araxes.ee` | `https` | 200 | 421 | 0.0085 | No | True | Safe / strict Host validation | Low |
| `araxes.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `estpak.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `estpak.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `fairyhosting.ee` | `https` | 301 | 200 | 0.0184 | No | False | Different response | Low |
| `fairyhosting.ee` | `http` | 301 | 403 | 0.035 | No | False | Safe / strict Host validation | Low |
| `neti.ee` | `https` | 302 | 503 | 0.0 | No | False | Different response | Low |
| `neti.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `xf.ee` | `https` | 200 | 301 | 0.008 | No | False | Redirects invalid Host | Low/Medium |
| `xf.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `kaubamaja.ee` | `https` | 302 | 403 | 0.8571 | No | False | Safe / strict Host validation | Low |
| `kaubamaja.ee` | `http` | 302 | 403 | 0.0346 | No | False | Safe / strict Host validation | Low |
| `lelosi.ee` | `https` | 200 | 403 | 0.026 | No | False | Safe / strict Host validation | Low |
| `lelosi.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `i-smith.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `i-smith.ee` | `http` | 200 | 403 | 0.0988 | No | False | Safe / strict Host validation | Low |
| `bauhaus.ee` | `https` | 301 | 403 | 0.715 | No | False | Safe / strict Host validation | Low |
| `bauhaus.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `fujitsu.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `fujitsu.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `telia.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `telia.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `emu.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `emu.ee` | `http` | 301 | 403 | 0.035 | No | False | Safe / strict Host validation | Low |
| `mor.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `mor.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `tervisekassa.ee` | `https` | 200 | 403 | 0.0273 | No | False | Safe / strict Host validation | Low |
| `tervisekassa.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `elron.ee` | `https` | 200 | 403 | 0.0349 | No | False | Safe / strict Host validation | Low |
| `elron.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `gototop.ee` | `https` | 200 | 200 | 0.041 | No | False | Different content with same status | Low/Medium |
| `gototop.ee` | `http` | 301 | 403 | 0.0455 | No | False | Safe / strict Host validation | Low |
| `coraltravel.ee` | `https` | 301 | 503 | 0.0 | No | False | Different response | Low |
| `coraltravel.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `tooltrade.ee` | `https` | 200 | 421 | 0.0089 | No | False | Safe / strict Host validation | Low |
| `tooltrade.ee` | `http` | 301 | 403 | 0.0129 | No | False | Safe / strict Host validation | Low |
| `eckeroline.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `eckeroline.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `mfa.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `mfa.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `tahm.ee` | `https` | 200 | 421 | 0.0078 | No | True | Safe / strict Host validation | Low |
| `tahm.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `jalgpall.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `jalgpall.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `shp.ee` | `https` | 404 | 307 | 0.2194 | No | False | Redirects invalid Host | Low/Medium |
| `shp.ee` | `http` | 307 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `itaku.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `itaku.ee` | `http` | 301 | 403 | 0.0456 | No | False | Safe / strict Host validation | Low |
| `e-krediidiinfo.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `e-krediidiinfo.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `luutar.ee` | `https` | 301 | 421 | 0.3948 | No | True | Safe / strict Host validation | Low |
| `luutar.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `myfitness.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `myfitness.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `vivatbet.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `vivatbet.ee` | `http` | 403 | 403 | 0.3163 | No | False | Safe / strict Host validation | Low |
| `topconnect.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `topconnect.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `biker.ee` | `https` | 200 | 421 | 0.0092 | No | True | Safe / strict Host validation | Low |
| `biker.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `rfer.ee` | `https` | 200 | 200 | 0.0 | No | False | Different content with same status | Low/Medium |
| `rfer.ee` | `http` | 308 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `tickets.ee` | `https` | 200 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `tickets.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `found.ee` | `https` | 307 | 307 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `found.ee` | `http` | 308 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `en.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `en.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `springriver.ee` | `https` | 301 | 200 | 0.027 | No | False | Different response | Low |
| `springriver.ee` | `http` | 301 | 403 | 0.0129 | No | False | Safe / strict Host validation | Low |
| `otsireisi.ee` | `https` | 301 | 403 | 0.4434 | No | False | Safe / strict Host validation | Low |
| `otsireisi.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `24-7fitness.ee` | `https` | 200 | 421 | 0.008 | No | True | Safe / strict Host validation | Low |
| `24-7fitness.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `smartech.ee` | `https` | 301 | 421 | 0.3923 | No | True | Safe / strict Host validation | Low |
| `smartech.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `tld.ee` | `https` | 200 | 200 | 0.4716 | No | False | Different content with same status | Low/Medium |
| `tld.ee` | `http` | 200 | 403 | 0.0412 | No | False | Safe / strict Host validation | Low |
| `8468.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `8468.ee` | `http` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `fill.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `fill.ee` | `http` | 301 | 403 | 0.0118 | No | False | Safe / strict Host validation | Low |
| `smartposti.ee` | `https` | 301 | None | 1.0 | No | False | Inconclusive | Low |
| `smartposti.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `karupoegpuhh.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `karupoegpuhh.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `chilli.ee` | `https` | 200 | 421 | 0.0085 | No | True | Safe / strict Host validation | Low |
| `chilli.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `tartumaraton.ee` | `https` | 200 | 421 | 0.0094 | No | True | Safe / strict Host validation | Low |
| `tartumaraton.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `amoremi.ee` | `https` | 301 | 421 | 0.3933 | No | True | Safe / strict Host validation | Low |
| `amoremi.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `shapelab.ee` | `https` | 200 | None | 0.0 | No | False | Inconclusive | Low |
| `shapelab.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `kuldnebors.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `kuldnebors.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `piletilevi.ee` | `https` | 301 | 301 | 0.7645 | Location, Headers | True | Possible Host header injection | High |
| `piletilevi.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `songtr.ee` | `https` | 302 | 421 | 0.1576 | No | True | Safe / strict Host validation | Low |
| `songtr.ee` | `http` | 302 | 403 | 0.0443 | No | False | Safe / strict Host validation | Low |
| `tktk.ee` | `https` | 301 | 200 | 0.0 | No | False | Different response | Low |
| `tktk.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `pagulasabi.ee` | `https` | 301 | 421 | 0.0716 | No | True | Safe / strict Host validation | Low |
| `pagulasabi.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `financeprofessional.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `financeprofessional.ee` | `http` | 403 | 403 | 0.3163 | No | False | Safe / strict Host validation | Low |
| `animehay.ee` | `https` | 200 | 403 | 0.0323 | No | False | Safe / strict Host validation | Low |
| `animehay.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `estonia.ee` | `https` | 200 | 200 | 1.0 | Headers | False | Weak Host validation | Medium |
| `estonia.ee` | `http` | 301 | 403 | 0.0456 | No | False | Safe / strict Host validation | Low |
| `cooppank.ee` | `https` | 308 | 404 | 0.0209 | No | False | Safe / strict Host validation | Low |
| `cooppank.ee` | `http` | 308 | 403 | 0.0014 | No | False | Safe / strict Host validation | Low |
| `elkdata.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `elkdata.ee` | `http` | 301 | 403 | 0.0114 | No | False | Safe / strict Host validation | Low |
| `elion.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `elion.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ikea.ee` | `https` | 403 | 403 | 0.0504 | No | False | Safe / strict Host validation | Low |
| `ikea.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `foreca.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `foreca.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `tpilet.ee` | `https` | 302 | 403 | 0.8097 | No | False | Safe / strict Host validation | Low |
| `tpilet.ee` | `http` | 302 | 403 | 0.0087 | No | False | Safe / strict Host validation | Low |
| `visa.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `visa.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `president.ee` | `https` | 200 | 403 | 0.0605 | No | False | Safe / strict Host validation | Low |
| `president.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `antehnika.ee` | `https` | 301 | 421 | 0.3938 | No | True | Safe / strict Host validation | Low |
| `antehnika.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `minuvalik.ee` | `https` | 200 | 200 | 0.9957 | No | False | Weak Host validation | Medium |
| `minuvalik.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `unibet.ee` | `https` | 301 | None | 0.0 | No | False | Inconclusive | Low |
| `unibet.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `tallinn.ee` | `https` | 301 | 403 | 0.264 | No | False | Safe / strict Host validation | Low |
| `tallinn.ee` | `http` | 301 | 403 | 0.0269 | No | False | Safe / strict Host validation | Low |
| `id.ee` | `https` | 301 | 403 | 0.2527 | No | False | Safe / strict Host validation | Low |
| `id.ee` | `http` | 301 | 403 | 0.0116 | No | False | Safe / strict Host validation | Low |
| `oomipood.ee` | `https` | 301 | 301 | 0.9329 | Location, Headers | True | Possible Host header injection | High |
| `oomipood.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `rahvaraamat.ee` | `https` | 307 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `rahvaraamat.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `rmk.ee` | `https` | 200 | 200 | 0.9908 | No | False | Weak Host validation | Medium |
| `rmk.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `machineryline.ee` | `https` | 200 | 404 | 0.0044 | No | False | Safe / strict Host validation | Low |
| `machineryline.ee` | `http` | 301 | 403 | 0.0181 | No | False | Safe / strict Host validation | Low |
| `automaailm.ee` | `https` | 200 | 404 | 0.0111 | No | False | Safe / strict Host validation | Low |
| `automaailm.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `eestipiir.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `eestipiir.ee` | `http` | 302 | 403 | 0.0359 | No | False | Safe / strict Host validation | Low |
| `lution.ee` | `https` | 200 | 403 | 0.055 | No | False | Safe / strict Host validation | Low |
| `lution.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `extranet.ee` | `https` | 200 | 421 | 0.0104 | No | False | Safe / strict Host validation | Low |
| `extranet.ee` | `http` | 301 | 403 | 0.0352 | No | False | Safe / strict Host validation | Low |
| `e-resident.gov.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `e-resident.gov.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `artun.ee` | `https` | 301 | 404 | 0.8219 | No | False | Safe / strict Host validation | Low |
| `artun.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `thepiratebay.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `thepiratebay.ee` | `http` | 200 | 403 | 0.0181 | No | False | Safe / strict Host validation | Low |
| `opera.ee` | `https` | 302 | 404 | 0.0 | No | False | Safe / strict Host validation | Low |
| `opera.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `kohvisemu.ee` | `https` | 301 | 403 | 0.346 | No | False | Safe / strict Host validation | Low |
| `kohvisemu.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `avariilised-autod.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `avariilised-autod.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `endla.ee` | `https` | 301 | 301 | 0.332 | Location, Headers | False | Possible Host header injection | High |
| `endla.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `cointr.ee` | `https` | 200 | 404 | 0.0194 | No | False | Safe / strict Host validation | Low |
| `cointr.ee` | `http` | 301 | 403 | 0.0048 | No | False | Safe / strict Host validation | Low |
| `etag.ee` | `https` | 200 | 421 | 0.008 | No | True | Safe / strict Host validation | Low |
| `etag.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `shope.ee` | `https` | 404 | 307 | 0.1034 | No | False | Redirects invalid Host | Low/Medium |
| `shope.ee` | `http` | 307 | 403 | 0.0312 | No | False | Safe / strict Host validation | Low |
| `youtube.ee` | `https` | 301 | 404 | 0.0 | No | False | Safe / strict Host validation | Low |
| `youtube.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `piletitasku.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `piletitasku.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `tahvel.edu.ee` | `https` | 200 | 404 | 0.0282 | No | False | Safe / strict Host validation | Low |
| `tahvel.edu.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `erm.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `erm.ee` | `http` | 301 | 403 | 0.0321 | No | False | Safe / strict Host validation | Low |
| `bet200.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `bet200.ee` | `http` | 403 | 403 | 0.3163 | No | False | Safe / strict Host validation | Low |
| `meis.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `meis.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `mkm.ee` | `https` | 200 | 403 | 0.0297 | No | False | Safe / strict Host validation | Low |
| `mkm.ee` | `http` | 301 | 403 | 0.0349 | No | False | Safe / strict Host validation | Low |
| `rik.ee` | `https` | 302 | 403 | 0.268 | No | False | Safe / strict Host validation | Low |
| `rik.ee` | `http` | 301 | 403 | 0.0269 | No | False | Safe / strict Host validation | Low |
| `jysk.ee` | `https` | 403 | 403 | 0.0426 | No | False | Safe / strict Host validation | Low |
| `jysk.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `ope.ee` | `https` | 301 | 404 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ope.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `annaabi.ee` | `https` | 200 | 403 | 0.0279 | No | False | Safe / strict Host validation | Low |
| `annaabi.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `arutle.ee` | `https` | 200 | 403 | 0.0412 | No | False | Safe / strict Host validation | Low |
| `arutle.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `aiguom.ee` | `https` | 200 | 421 | 0.0102 | No | True | Safe / strict Host validation | Low |
| `aiguom.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `crime.ee` | `https` | 200 | 200 | 0.0064 | No | False | Different content with same status | Low/Medium |
| `crime.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `ohtuleht.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ohtuleht.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `mileedi.ee` | `https` | 200 | 301 | 0.0213 | Location, Headers | False | Possible Host header injection | High |
| `mileedi.ee` | `http` | 301 | 403 | 0.0295 | No | False | Safe / strict Host validation | Low |
| `seti.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `seti.ee` | `http` | 301 | 403 | 0.0403 | No | False | Safe / strict Host validation | Low |
| `stena.ee` | `https` | 301 | 502 | 0.4479 | No | False | Different response | Low |
| `stena.ee` | `http` | 301 | 403 | 0.0118 | No | False | Safe / strict Host validation | Low |
| `topvaruosad.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `topvaruosad.ee` | `http` | 308 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `konverter.ee` | `https` | 301 | 421 | 0.3938 | No | True | Safe / strict Host validation | Low |
| `konverter.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `host.ee` | `https` | 200 | 403 | 0.0341 | No | False | Safe / strict Host validation | Low |
| `host.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `olympic-casino.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `olympic-casino.ee` | `http` | 403 | 403 | 0.3163 | No | False | Safe / strict Host validation | Low |
| `spaestonia.ee` | `https` | 200 | 421 | 0.0113 | No | True | Safe / strict Host validation | Low |
| `spaestonia.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `depo.ee` | `https` | 200 | 421 | 0.0091 | No | False | Safe / strict Host validation | Low |
| `depo.ee` | `http` | 301 | 403 | 0.0139 | No | False | Safe / strict Host validation | Low |
| `omniva.ee` | `https` | 308 | 403 | 0.1516 | No | False | Safe / strict Host validation | Low |
| `omniva.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `aeromotors.ee` | `https` | 200 | 403 | 0.0225 | No | False | Safe / strict Host validation | Low |
| `aeromotors.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `intercars24.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `intercars24.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `rde.ee` | `https` | 301 | 403 | 0.3489 | No | False | Safe / strict Host validation | Low |
| `rde.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `hawaii.ee` | `https` | 200 | 421 | 0.0075 | No | False | Safe / strict Host validation | Low |
| `hawaii.ee` | `http` | 301 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `autoportaal.ee` | `https` | 200 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `autoportaal.ee` | `http` | 301 | 403 | 0.046 | No | False | Safe / strict Host validation | Low |
| `carlnet.ee` | `https` | 302 | 421 | 0.0 | No | False | Safe / strict Host validation | Low |
| `carlnet.ee` | `http` | 301 | 403 | 0.0353 | No | False | Safe / strict Host validation | Low |
| `ecosh.ee` | `https` | 200 | 421 | 0.0095 | No | True | Safe / strict Host validation | Low |
| `ecosh.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `kaup24.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `kaup24.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `compic.ee` | `https` | 302 | 421 | 0.4007 | No | False | Safe / strict Host validation | Low |
| `compic.ee` | `http` | 302 | 403 | 0.013 | No | False | Safe / strict Host validation | Low |
| `reimann.ee` | `https` | 403 | 403 | 0.8714 | No | False | Safe / strict Host validation | Low |
| `reimann.ee` | `http` | 404 | 403 | 0.0362 | No | False | Safe / strict Host validation | Low |
| `spavarska.ee` | `https` | 200 | 421 | 0.0089 | No | True | Safe / strict Host validation | Low |
| `spavarska.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `onoff.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `onoff.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `benu.ee` | `https` | 301 | 403 | 0.4537 | No | False | Safe / strict Host validation | Low |
| `benu.ee` | `http` | 301 | 403 | 0.0339 | No | False | Safe / strict Host validation | Low |
| `omega.ee` | `https` | 200 | 421 | 0.0125 | No | True | Safe / strict Host validation | Low |
| `omega.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `mo.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `mo.ee` | `http` | 301 | 403 | 0.0114 | No | False | Safe / strict Host validation | Low |
| `veoseleht.ee` | `https` | 200 | 421 | 0.0094 | No | False | Safe / strict Host validation | Low |
| `veoseleht.ee` | `http` | 301 | 403 | 0.0339 | No | False | Safe / strict Host validation | Low |
| `bet365.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `bet365.ee` | `http` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `ehituseabc.ee` | `https` | 301 | 503 | 0.0 | No | False | Different response | Low |
| `ehituseabc.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `veebimajutus.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `veebimajutus.ee` | `http` | 301 | 403 | 0.0439 | No | False | Safe / strict Host validation | Low |
| `geenius.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `geenius.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `selver.ee` | `https` | 301 | 403 | 0.7829 | No | False | Safe / strict Host validation | Low |
| `selver.ee` | `http` | 301 | 403 | 0.0025 | No | False | Safe / strict Host validation | Low |
| `evr.ee` | `https` | 302 | 403 | 0.3583 | No | False | Safe / strict Host validation | Low |
| `evr.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `douglas.ee` | `https` | 301 | 503 | 0.303 | No | False | Different response | Low |
| `douglas.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `tamectrade.ee` | `https` | 200 | 421 | 0.0092 | No | True | Safe / strict Host validation | Low |
| `tamectrade.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `elamusspa.ee` | `https` | 200 | 421 | 0.0089 | No | True | Safe / strict Host validation | Low |
| `elamusspa.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `digisoov.ee` | `https` | 200 | 200 | 0.0078 | No | False | Different content with same status | Low/Medium |
| `digisoov.ee` | `http` | 200 | 403 | 0.0321 | No | False | Safe / strict Host validation | Low |
| `sk.ee` | `https` | 302 | None | 1.0 | No | False | Inconclusive | Low |
| `sk.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `apotheka.ee` | `https` | 301 | 301 | 0.9446 | Location, Headers | True | Possible Host header injection | High |
| `apotheka.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `adblock.ee` | `https` | 301 | 404 | 0.4339 | No | False | Safe / strict Host validation | Low |
| `adblock.ee` | `http` | 404 | 403 | 0.0768 | No | False | Safe / strict Host validation | Low |
| `sci-hub.ee` | `https` | 200 | 403 | 0.0388 | No | False | Safe / strict Host validation | Low |
| `sci-hub.ee` | `http` | 200 | 403 | 0.0304 | No | False | Safe / strict Host validation | Low |
| `jukukeskus.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `jukukeskus.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `charlot.ee` | `https` | 200 | 403 | 0.045 | No | False | Safe / strict Host validation | Low |
| `charlot.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `lukuexpert.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `lukuexpert.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `elektrikell.ee` | `https` | 301 | 404 | 1.0 | No | False | Safe / strict Host validation | Low |
| `elektrikell.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `sky.ee` | `https` | 200 | 200 | 0.9976 | Headers | False | Weak Host validation | Medium |
| `sky.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `emta.ee` | `https` | 200 | 403 | 0.0302 | No | False | Safe / strict Host validation | Low |
| `emta.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `arvutiabi-esoft.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `arvutiabi-esoft.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `arvid.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `arvid.ee` | `http` | 200 | 403 | 0.1025 | No | False | Safe / strict Host validation | Low |
| `autoline.ee` | `https` | 200 | 404 | 0.0044 | No | False | Safe / strict Host validation | Low |
| `autoline.ee` | `http` | 301 | 403 | 0.1065 | No | False | Safe / strict Host validation | Low |
| `vanemuine.ee` | `https` | 200 | 421 | 0.0086 | No | True | Safe / strict Host validation | Low |
| `vanemuine.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `ega.ee` | `https` | 200 | 421 | 0.0099 | No | True | Safe / strict Host validation | Low |
| `ega.ee` | `http` | 301 | 403 | 0.0321 | No | False | Safe / strict Host validation | Low |
| `elektrum.ee` | `https` | 302 | None | 0.0 | No | False | Inconclusive | Low |
| `elektrum.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `mini.ee` | `https` | 301 | 503 | 0.1323 | No | False | Different response | Low |
| `mini.ee` | `http` | 301 | 403 | 0.0334 | No | False | Safe / strict Host validation | Low |
| `ttja.ee` | `https` | 200 | 403 | 0.031 | No | False | Safe / strict Host validation | Low |
| `ttja.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `aripaev.ee` | `https` | 302 | 403 | 0.3583 | No | False | Safe / strict Host validation | Low |
| `aripaev.ee` | `http` | 302 | 403 | 0.025 | No | False | Safe / strict Host validation | Low |
| `eki.ee` | `https` | 200 | 421 | 0.0109 | No | True | Safe / strict Host validation | Low |
| `eki.ee` | `http` | 301 | 403 | 0.0422 | No | False | Safe / strict Host validation | Low |
| `diil.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `diil.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `gazeta.ee` | `https` | 200 | 421 | 0.0102 | No | True | Safe / strict Host validation | Low |
| `gazeta.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `kennelliit.ee` | `https` | 200 | 403 | 0.0715 | No | False | Safe / strict Host validation | Low |
| `kennelliit.ee` | `http` | 307 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `airguru.ee` | `https` | 403 | 403 | 0.0503 | No | False | Safe / strict Host validation | Low |
| `airguru.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `elke.ee` | `https` | 301 | 200 | 0.0 | No | False | Different response | Low |
| `elke.ee` | `http` | 301 | 403 | 0.0456 | No | False | Safe / strict Host validation | Low |
| `mascus.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `mascus.ee` | `http` | 301 | 403 | 0.0142 | No | False | Safe / strict Host validation | Low |
| `super-hobby.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `super-hobby.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `teliatv.ee` | `https` | 301 | 403 | 0.8493 | No | False | Safe / strict Host validation | Low |
| `teliatv.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `rimi.ee` | `https` | 301 | 421 | 0.0 | No | False | Safe / strict Host validation | Low |
| `rimi.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `apollo.ee` | `https` | 301 | 421 | 0.3943 | No | True | Safe / strict Host validation | Low |
| `apollo.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `valgamaa.ee` | `https` | 200 | 421 | 0.0183 | No | True | Safe / strict Host validation | Low |
| `valgamaa.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `maxima.ee` | `https` | 301 | 404 | 0.8219 | No | False | Safe / strict Host validation | Low |
| `maxima.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `kino.ee` | `https` | 200 | 404 | 0.0256 | No | False | Safe / strict Host validation | Low |
| `kino.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `eperearstikeskus.ee` | `https` | 302 | 302 | 1.0 | Location, Headers | False | Possible Host header injection | High |
| `eperearstikeskus.ee` | `http` | 301 | 403 | 0.0325 | No | False | Safe / strict Host validation | Low |
| `rara.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `rara.ee` | `http` | 301 | 403 | 0.0117 | No | False | Safe / strict Host validation | Low |
| `k-rauta.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `k-rauta.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `vinted.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `vinted.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `lemm.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `lemm.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `up.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `up.ee` | `http` | 301 | 403 | 0.0353 | No | False | Safe / strict Host validation | Low |
| `s.ee` | `https` | 200 | 403 | 0.0253 | No | False | Safe / strict Host validation | Low |
| `s.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `eis.ee` | `https` | 200 | 403 | 0.0233 | No | False | Safe / strict Host validation | Low |
| `eis.ee` | `http` | 301 | 403 | 0.0117 | No | False | Safe / strict Host validation | Low |
| `sportsdirect.ee` | `https` | 301 | 400 | 0.0 | No | False | Safe / strict Host validation | Low |
| `sportsdirect.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `freemeteo.ee` | `https` | 200 | 200 | 0.8594 | No | False | Different content with same status | Low/Medium |
| `freemeteo.ee` | `http` | 301 | 403 | 0.0456 | No | False | Safe / strict Host validation | Low |
| `redbulltourbus.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `redbulltourbus.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `eesti.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `eesti.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `optibet.ee` | `https` | 403 | 403 | 0.0403 | No | False | Safe / strict Host validation | Low |
| `optibet.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `energia.ee` | `https` | 301 | 403 | 0.2637 | No | False | Safe / strict Host validation | Low |
| `energia.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `agri.ee` | `https` | 200 | 403 | 0.0277 | No | False | Safe / strict Host validation | Low |
| `agri.ee` | `http` | 301 | 403 | 0.0072 | No | False | Safe / strict Host validation | Low |
| `sony.ee` | `https` | 301 | 301 | 1.0 | Location, Headers | False | Possible Host header injection | High |
| `sony.ee` | `http` | 301 | 403 | 0.0101 | No | False | Safe / strict Host validation | Low |
| `save24.ee` | `https` | 403 | 403 | 0.0426 | No | False | Safe / strict Host validation | Low |
| `save24.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `taskutark.ee` | `https` | 301 | 403 | 0.7829 | No | False | Safe / strict Host validation | Low |
| `taskutark.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `funbox.ee` | `https` | 200 | 403 | 0.0332 | No | False | Safe / strict Host validation | Low |
| `funbox.ee` | `http` | 301 | 403 | 0.0163 | No | False | Safe / strict Host validation | Low |
| `tehnikastuudio.ee` | `https` | 200 | 421 | 0.0087 | No | True | Safe / strict Host validation | Low |
| `tehnikastuudio.ee` | `http` | 301 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `ekm.ee` | `https` | 301 | 302 | 0.0 | Location, Headers | False | Possible Host header injection | High |
| `ekm.ee` | `http` | 301 | 403 | 0.0163 | No | False | Safe / strict Host validation | Low |
| `wavecom.ee` | `https` | 200 | 421 | 0.0099 | No | True | Safe / strict Host validation | Low |
| `wavecom.ee` | `http` | 308 | 403 | 0.0123 | No | False | Safe / strict Host validation | Low |
| `linktr.ee` | `https` | 200 | 421 | 0.0032 | No | False | Safe / strict Host validation | Low |
| `linktr.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `tln.edu.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `tln.edu.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `sonaveeb.ee` | `https` | 200 | 421 | 0.013 | No | True | Safe / strict Host validation | Low |
| `sonaveeb.ee` | `http` | 301 | 403 | 0.0332 | No | False | Safe / strict Host validation | Low |
| `fiber.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `fiber.ee` | `http` | 302 | 403 | 0.0347 | No | False | Safe / strict Host validation | Low |
| `bmwclub.ee` | `https` | 200 | 421 | 0.0133 | No | True | Safe / strict Host validation | Low |
| `bmwclub.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `momondo.ee` | `https` | 301 | 421 | 0.0541 | No | False | Safe / strict Host validation | Low |
| `momondo.ee` | `http` | 301 | 403 | 0.0385 | No | False | Safe / strict Host validation | Low |
| `nlib.ee` | `https` | 301 | 503 | 0.0 | No | False | Different response | Low |
| `nlib.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `germalo.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `germalo.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `startupestonia.ee` | `https` | 200 | 403 | 0.031 | No | False | Safe / strict Host validation | Low |
| `startupestonia.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `pleier.ee` | `https` | 200 | 503 | 0.0054 | No | False | Different response | Low |
| `pleier.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `swedbank.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `swedbank.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `mnt.ee` | `https` | 301 | 400 | 0.3855 | No | True | Safe / strict Host validation | Low |
| `mnt.ee` | `http` | 301 | 403 | 0.0141 | No | False | Safe / strict Host validation | Low |
| `edss.ee` | `https` | 301 | 301 | 1.0 | Location, Headers | False | Possible Host header injection | High |
| `edss.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `lin.ee` | `https` | 404 | 404 | 0.1722 | No | False | Safe / strict Host validation | Low |
| `lin.ee` | `http` | 308 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `turniir.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `turniir.ee` | `http` | 200 | 403 | 0.0313 | No | False | Safe / strict Host validation | Low |
| `ts.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ts.ee` | `http` | 301 | 403 | 0.0117 | No | False | Safe / strict Host validation | Low |
| `kirj.ee` | `https` | 307 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `kirj.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `hhanime3d.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `hhanime3d.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `norby.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `norby.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `delfi.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `delfi.ee` | `http` | 301 | 403 | 0.0252 | No | False | Safe / strict Host validation | Low |
| `cvkeskus.ee` | `https` | 301 | 404 | 0.0 | No | False | Safe / strict Host validation | Low |
| `cvkeskus.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `data.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `data.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `autokaubad24.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `autokaubad24.ee` | `http` | 403 | 403 | 0.0298 | No | False | Safe / strict Host validation | Low |
| `kae.edu.ee` | `https` | 404 | 404 | 0.0454 | No | False | Safe / strict Host validation | Low |
| `kae.edu.ee` | `http` | 404 | 403 | 0.0187 | No | False | Safe / strict Host validation | Low |
| `1it.ee` | `https` | 200 | 421 | 0.0085 | No | True | Safe / strict Host validation | Low |
| `1it.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `kingitus.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `kingitus.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `home4you.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `home4you.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `mugavik.ee` | `https` | 200 | 403 | 0.0252 | No | False | Safe / strict Host validation | Low |
| `mugavik.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `linnagalerii.ee` | `https` | 200 | 421 | 0.0087 | No | False | Safe / strict Host validation | Low |
| `linnagalerii.ee` | `http` | 301 | 403 | 0.0338 | No | False | Safe / strict Host validation | Low |
| `google.ee` | `https` | 301 | 404 | 0.0308 | No | False | Safe / strict Host validation | Low |
| `google.ee` | `http` | 301 | 403 | 0.0792 | No | False | Safe / strict Host validation | Low |
| `olybet.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `olybet.ee` | `http` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `uueduudised.ee` | `https` | 200 | 421 | 0.0088 | No | True | Safe / strict Host validation | Low |
| `uueduudised.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `tolg.ee` | `https` | 302 | 404 | 0.0 | No | False | Safe / strict Host validation | Low |
| `tolg.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `interframe.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `interframe.ee` | `http` | 301 | 403 | 0.0122 | No | False | Safe / strict Host validation | Low |
| `alleegalerii.ee` | `https` | 200 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `alleegalerii.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `td.ee` | `https` | 200 | 403 | 0.0429 | No | False | Safe / strict Host validation | Low |
| `td.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `eek.ee` | `https` | 200 | 200 | 0.0349 | Cookie, Headers | False | Possible Host header injection | High |
| `eek.ee` | `http` | 301 | 403 | 0.0354 | No | False | Safe / strict Host validation | Low |
| `kadi.ee` | `https` | 200 | 421 | 0.0165 | No | True | Safe / strict Host validation | Low |
| `kadi.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `bonami.ee` | `https` | 301 | None | 0.0 | No | False | Inconclusive | Low |
| `bonami.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `avaandmed.ee` | `https` | 502 | 502 | 1.0 | No | False | Different response | Low |
| `avaandmed.ee` | `http` | 301 | 403 | 0.0311 | No | False | Safe / strict Host validation | Low |
| `iha.ee` | `https` | 301 | 403 | 0.4135 | No | False | Safe / strict Host validation | Low |
| `iha.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `eenet.ee` | `https` | 302 | 403 | 0.2653 | No | False | Safe / strict Host validation | Low |
| `eenet.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `tartu.ee` | `https` | 301 | 403 | 0.2125 | No | False | Safe / strict Host validation | Low |
| `tartu.ee` | `http` | 301 | 403 | 0.0117 | No | False | Safe / strict Host validation | Low |
| `intermedia.ee` | `https` | 200 | 421 | 0.0027 | No | False | Safe / strict Host validation | Low |
| `intermedia.ee` | `http` | 301 | 403 | 0.0139 | No | False | Safe / strict Host validation | Low |
| `kolab.ee` | `https` | 200 | 403 | 0.0135 | No | False | Safe / strict Host validation | Low |
| `kolab.ee` | `http` | 301 | 403 | 0.0339 | No | False | Safe / strict Host validation | Low |
| `moobel1.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `moobel1.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `espak.ee` | `https` | 200 | 421 | 0.0081 | No | True | Safe / strict Host validation | Low |
| `espak.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `kaitsevaeteenistus.ee` | `https` | 303 | 403 | 0.0875 | No | False | Safe / strict Host validation | Low |
| `kaitsevaeteenistus.ee` | `http` | 301 | 403 | 0.0278 | No | False | Safe / strict Host validation | Low |
| `gemoss.ee` | `https` | 403 | 403 | 0.042 | No | False | Safe / strict Host validation | Low |
| `gemoss.ee` | `http` | 302 | 403 | 0.0259 | No | False | Safe / strict Host validation | Low |
| `diggers.ee` | `https` | 200 | 403 | 0.2155 | No | False | Safe / strict Host validation | Low |
| `diggers.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `ria.ee` | `https` | 200 | 403 | 0.0358 | No | False | Safe / strict Host validation | Low |
| `ria.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `postimees.ee` | `https` | 301 | 503 | 0.0 | No | False | Different response | Low |
| `postimees.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `webmail.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `webmail.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `nutz.ee` | `https` | 403 | 403 | 0.027 | No | False | Safe / strict Host validation | Low |
| `nutz.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `eestipank.ee` | `https` | 307 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `eestipank.ee` | `http` | 301 | 403 | 0.0272 | No | False | Safe / strict Host validation | Low |
| `levira.ee` | `https` | 301 | 404 | 0.0 | No | False | Safe / strict Host validation | Low |
| `levira.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `pets.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `pets.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `telegram.ee` | `https` | 301 | 302 | 1.0 | Location, Headers | False | Possible Host header injection | High |
| `telegram.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `kalake.ee` | `https` | 200 | 301 | 0.0 | Cookie, Headers | False | Possible Host header injection | High |
| `kalake.ee` | `http` | 301 | 403 | 0.042 | No | False | Safe / strict Host validation | Low |
| `eestikonverentsikeskus.ee` | `https` | 200 | 421 | 0.0031 | No | True | Safe / strict Host validation | Low |
| `eestikonverentsikeskus.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `elisa.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `elisa.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `mail.ee` | `https` | 301 | 302 | 0.8592 | Headers | False | Redirects invalid Host | Low/Medium |
| `mail.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `joinup.ee` | `https` | 301 | 403 | 0.3103 | No | False | Safe / strict Host validation | Low |
| `joinup.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `valitsus.ee` | `https` | 200 | 403 | 0.029 | No | False | Safe / strict Host validation | Low |
| `valitsus.ee` | `http` | 301 | 403 | 0.0269 | No | False | Safe / strict Host validation | Low |
| `smartpost.ee` | `https` | 301 | None | 1.0 | No | False | Inconclusive | Low |
| `smartpost.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `techtr.ee` | `https` | 403 | 200 | 0.0075 | No | False | Different response | Low |
| `techtr.ee` | `http` | 301 | 403 | 0.0005 | No | False | Safe / strict Host validation | Low |
| `otsintood.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `otsintood.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `romu.ee` | `https` | 301 | 421 | 0.0 | No | False | Safe / strict Host validation | Low |
| `romu.ee` | `http` | 301 | 403 | 0.0129 | No | False | Safe / strict Host validation | Low |
| `err.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `err.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `okidoki.ee` | `https` | 403 | 403 | 0.0426 | No | False | Safe / strict Host validation | Low |
| `okidoki.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `kitsune.ee` | `https` | 200 | 404 | 0.033 | No | False | Safe / strict Host validation | Low |
| `kitsune.ee` | `http` | 200 | 403 | 0.0578 | No | False | Safe / strict Host validation | Low |
| `riigikogu.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `riigikogu.ee` | `http` | 301 | 403 | 0.0271 | No | False | Safe / strict Host validation | Low |
| `klick.ee` | `https` | 301 | 301 | 1.0 | Location, Headers | False | Possible Host header injection | High |
| `klick.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `rue.ee` | `https` | 200 | 403 | 0.0355 | No | False | Safe / strict Host validation | Low |
| `rue.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `evs.ee` | `https` | 301 | 500 | 0.0055 | No | False | Different response | Low |
| `evs.ee` | `http` | 301 | 500 | 0.0055 | No | False | Different response | Low |
| `projektid.edu.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `projektid.edu.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `stokker.ee` | `https` | 301 | 200 | 0.0031 | Body | False | Possible Host header injection | Medium |
| `stokker.ee` | `http` | 301 | 403 | 0.0311 | No | False | Safe / strict Host validation | Low |
| `kodumasinad.ee` | `https` | 301 | 503 | 0.0 | No | False | Different response | Low |
| `kodumasinad.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `vesikoer.ee` | `https` | 200 | 200 | 0.0597 | No | False | Different content with same status | Low/Medium |
| `vesikoer.ee` | `http` | 200 | 403 | 0.0825 | No | False | Safe / strict Host validation | Low |
| `ivm.ee` | `https` | 200 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `ivm.ee` | `http` | 302 | 403 | 0.0363 | No | False | Safe / strict Host validation | Low |
| `zone.ee` | `https` | 301 | 302 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `zone.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `euronics.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `euronics.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `planet.ee` | `https` | 301 | 302 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `planet.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `alexela.ee` | `https` | 301 | 421 | 0.3933 | No | True | Safe / strict Host validation | Low |
| `alexela.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `spin.ee` | `https` | 200 | 421 | 0.0083 | No | False | Safe / strict Host validation | Low |
| `spin.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `rmit.ee` | `https` | 200 | 403 | 0.0326 | No | False | Safe / strict Host validation | Low |
| `rmit.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `krfitness.ee` | `https` | 200 | 421 | 0.0101 | No | True | Safe / strict Host validation | Low |
| `krfitness.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `hoolduskeskus.ee` | `https` | 301 | 421 | 0.0 | No | False | Safe / strict Host validation | Low |
| `hoolduskeskus.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `mcaf.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `mcaf.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `infonet.ee` | `https` | 200 | 401 | 0.0285 | No | False | Different response | Low |
| `infonet.ee` | `http` | 302 | 403 | 0.0343 | No | False | Safe / strict Host validation | Low |
| `stat.ee` | `https` | 301 | 400 | 0.2067 | No | False | Safe / strict Host validation | Low |
| `stat.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `voco.ee` | `https` | 200 | 421 | 0.0101 | No | True | Safe / strict Host validation | Low |
| `voco.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `ul.ee` | `https` | 301 | 421 | 0.2857 | No | False | Safe / strict Host validation | Low |
| `ul.ee` | `http` | 301 | 403 | 0.0354 | No | False | Safe / strict Host validation | Low |
| `juhend.ee` | `https` | 308 | 404 | 0.8435 | No | False | Safe / strict Host validation | Low |
| `juhend.ee` | `http` | 308 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `joogastuudio.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `joogastuudio.ee` | `http` | 301 | 403 | 0.0324 | No | False | Safe / strict Host validation | Low |
| `unisend.ee` | `https` | 200 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `unisend.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `lank.ee` | `https` | 200 | 421 | 0.0115 | No | False | Safe / strict Host validation | Low |
| `lank.ee` | `http` | 301 | 403 | 0.0354 | No | False | Safe / strict Host validation | Low |
| `itcollege.ee` | `https` | 301 | 301 | 0.9483 | Location, Headers | True | Possible Host header injection | High |
| `itcollege.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `soov.ee` | `https` | 200 | 403 | 0.0251 | No | False | Safe / strict Host validation | Low |
| `soov.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `notino.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `notino.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `realkeskus.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `realkeskus.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `rate.ee` | `https` | 302 | 200 | 0.0 | No | False | Different response | Low |
| `rate.ee` | `http` | 301 | 403 | 0.0109 | No | False | Safe / strict Host validation | Low |
| `ladu24.ee` | `https` | 301 | 421 | 0.3943 | No | True | Safe / strict Host validation | Low |
| `ladu24.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `kriis.ee` | `https` | 200 | 403 | 0.0266 | No | False | Safe / strict Host validation | Low |
| `kriis.ee` | `http` | 301 | 403 | 0.0116 | No | False | Safe / strict Host validation | Low |
| `beeserver.ee` | `https` | 301 | 421 | 0.2821 | No | False | Safe / strict Host validation | Low |
| `beeserver.ee` | `http` | 301 | 403 | 0.0347 | No | False | Safe / strict Host validation | Low |
| `wirtgen.ee` | `https` | 301 | 421 | 0.2821 | No | False | Safe / strict Host validation | Low |
| `wirtgen.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `lavendelloomeruum.ee` | `https` | 200 | 200 | 0.0114 | No | False | Different content with same status | Low/Medium |
| `lavendelloomeruum.ee` | `http` | 200 | 403 | 0.0162 | No | False | Safe / strict Host validation | Low |
| `eestiloto.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `eestiloto.ee` | `http` | 403 | 403 | 0.32 | No | False | Safe / strict Host validation | Low |
| `mil.ee` | `https` | 200 | 403 | 0.0197 | No | False | Safe / strict Host validation | Low |
| `mil.ee` | `http` | 301 | 403 | 0.0268 | No | False | Safe / strict Host validation | Low |
| `maaamet.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `maaamet.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `ioc.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `ioc.ee` | `http` | 301 | 403 | 0.0439 | No | False | Safe / strict Host validation | Low |
| `fitpoint.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `fitpoint.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `open.ee` | `https` | 200 | 200 | 0.0018 | No | False | Different content with same status | Low/Medium |
| `open.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `ap3.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `ap3.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `leiutuba.ee` | `https` | 200 | 421 | 0.0085 | No | True | Safe / strict Host validation | Low |
| `leiutuba.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `javico.ee` | `https` | 301 | 421 | 0.2857 | No | False | Safe / strict Host validation | Low |
| `javico.ee` | `http` | 301 | 403 | 0.0139 | No | False | Safe / strict Host validation | Low |
| `tootukassa.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `tootukassa.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `barbora.ee` | `https` | 200 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `barbora.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `ra.ee` | `https` | 301 | 200 | 0.0102 | No | False | Different response | Low |
| `ra.ee` | `http` | 301 | 403 | 0.0109 | No | False | Safe / strict Host validation | Low |
| `fi.ee` | `https` | 301 | 403 | 0.2156 | No | False | Safe / strict Host validation | Low |
| `fi.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `pilet.ee` | `https` | 200 | 403 | 0.0208 | No | False | Safe / strict Host validation | Low |
| `pilet.ee` | `http` | 308 | 403 | 0.0128 | No | False | Safe / strict Host validation | Low |
| `hiiuleht.ee` | `https` | 200 | 421 | 0.003 | No | True | Safe / strict Host validation | Low |
| `hiiuleht.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `lenne.ee` | `https` | 200 | 421 | 0.0097 | No | True | Safe / strict Host validation | Low |
| `lenne.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `rakvereteater.ee` | `https` | 200 | 400 | 0.0154 | No | False | Safe / strict Host validation | Low |
| `rakvereteater.ee` | `http` | 301 | 403 | 0.0118 | No | False | Safe / strict Host validation | Low |
| `pmo.ee` | `https` | 200 | 503 | 0.0 | No | False | Different response | Low |
| `pmo.ee` | `http` | 200 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `c7.ee` | `https` | 301 | 404 | 0.0782 | No | False | Safe / strict Host validation | Low |
| `c7.ee` | `http` | 301 | 403 | 0.0025 | No | False | Safe / strict Host validation | Low |
| `nami-nami.ee` | `https` | 200 | 421 | 0.0117 | No | False | Safe / strict Host validation | Low |
| `nami-nami.ee` | `http` | 301 | 403 | 0.0133 | No | False | Safe / strict Host validation | Low |
| `zalando-lounge.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `zalando-lounge.ee` | `http` | 301 | 403 | 0.0101 | No | False | Safe / strict Host validation | Low |
| `sportland.ee` | `https` | 200 | 403 | 0.0261 | No | False | Safe / strict Host validation | Low |
| `sportland.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `coop.ee` | `https` | 302 | 421 | 0.4874 | No | True | Safe / strict Host validation | Low |
| `coop.ee` | `http` | 302 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `kangadzungel.ee` | `https` | 301 | 403 | 0.2497 | No | False | Safe / strict Host validation | Low |
| `kangadzungel.ee` | `http` | 301 | 403 | 0.0253 | No | False | Safe / strict Host validation | Low |
| `vitateka.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `vitateka.ee` | `http` | 301 | 403 | 0.0232 | No | False | Safe / strict Host validation | Low |
| `linnateater.ee` | `https` | 200 | 421 | 0.0094 | No | True | Safe / strict Host validation | Low |
| `linnateater.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `unblockedgames.ee` | `https` | 200 | 403 | 0.0283 | No | False | Safe / strict Host validation | Low |
| `unblockedgames.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `on24.ee` | `https` | 301 | 400 | 0.3669 | No | True | Safe / strict Host validation | Low |
| `on24.ee` | `http` | 301 | 403 | 0.0402 | No | False | Safe / strict Host validation | Low |
| `teatmik.ee` | `https` | 301 | 421 | 0.2321 | No | True | Safe / strict Host validation | Low |
| `teatmik.ee` | `http` | 301 | 403 | 0.0353 | No | False | Safe / strict Host validation | Low |
| `dyson.com.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `dyson.com.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `sansan.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `sansan.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `babycity.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `babycity.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `latene.ee` | `https` | 200 | 403 | 0.031 | No | False | Safe / strict Host validation | Low |
| `latene.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `lombard24.ee` | `https` | 200 | 421 | 0.0097 | No | True | Safe / strict Host validation | Low |
| `lombard24.ee` | `http` | 301 | 403 | 0.0136 | No | False | Safe / strict Host validation | Low |
| `vikingline.ee` | `https` | 301 | 503 | 0.0 | No | False | Different response | Low |
| `vikingline.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `loginet.ee` | `https` | 302 | 400 | 0.1071 | No | False | Safe / strict Host validation | Low |
| `loginet.ee` | `http` | 302 | 403 | 0.014 | No | False | Safe / strict Host validation | Low |
| `dbweb.ee` | `https` | 200 | 421 | 0.0133 | No | False | Safe / strict Host validation | Low |
| `dbweb.ee` | `http` | 302 | 403 | 0.036 | No | False | Safe / strict Host validation | Low |
| `tinyurl.ee` | `https` | 200 | 403 | 0.0487 | No | False | Safe / strict Host validation | Low |
| `tinyurl.ee` | `http` | 301 | 403 | 0.0507 | No | False | Safe / strict Host validation | Low |
| `hom.ee` | `https` | 200 | 200 | 0.0139 | No | False | Different content with same status | Low/Medium |
| `hom.ee` | `http` | 301 | 403 | 0.0312 | No | False | Safe / strict Host validation | Low |
| `venten.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `venten.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `forum.ee` | `https` | 200 | 403 | 0.0365 | No | False | Safe / strict Host validation | Low |
| `forum.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `stockmann.ee` | `https` | 403 | 403 | 0.1567 | No | False | Safe / strict Host validation | Low |
| `stockmann.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `mariacasino.ee` | `https` | 301 | None | 0.0 | No | False | Inconclusive | Low |
| `mariacasino.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `lugeja.ee` | `https` | 301 | 301 | 0.9697 | No | True | Redirects invalid Host | Low |
| `lugeja.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `upload.ee` | `https` | 301 | 200 | 0.0197 | No | False | Different response | Low |
| `upload.ee` | `http` | 301 | 403 | 0.0352 | No | False | Safe / strict Host validation | Low |
| `vurtsid.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `vurtsid.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `eunet.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `eunet.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `fv.ee` | `https` | 301 | 302 | 0.8592 | Location, Headers | False | Possible Host header injection | High |
| `fv.ee` | `http` | 302 | 403 | 0.0346 | No | False | Safe / strict Host validation | Low |
| `tehik.ee` | `https` | 301 | 403 | 0.3489 | No | False | Safe / strict Host validation | Low |
| `tehik.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `tradehouse.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `tradehouse.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `lnkm.ee` | `https` | 200 | 200 | 0.0303 | No | False | Different content with same status | Low/Medium |
| `lnkm.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `raamatukoi.ee` | `https` | 200 | 200 | 0.0 | No | False | Different content with same status | Low/Medium |
| `raamatukoi.ee` | `http` | 308 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `coff.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `coff.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `magaziin.ee` | `https` | 200 | None | 0.0 | No | False | Inconclusive | Low |
| `magaziin.ee` | `http` | 301 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `beautyshop.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `beautyshop.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `xtom.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `xtom.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `stv.ee` | `https` | 200 | 302 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `stv.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `envir.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `envir.ee` | `http` | 301 | 403 | 0.0335 | No | False | Safe / strict Host validation | Low |
| `pets24.ee` | `https` | 308 | 403 | 0.3425 | No | False | Safe / strict Host validation | Low |
| `pets24.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `voodi.ee` | `https` | 200 | 403 | 0.0383 | No | False | Safe / strict Host validation | Low |
| `voodi.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `epa.ee` | `https` | 302 | 403 | 0.268 | No | False | Safe / strict Host validation | Low |
| `epa.ee` | `http` | 301 | 403 | 0.0349 | No | False | Safe / strict Host validation | Low |
| `maitsevtartu.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `maitsevtartu.ee` | `http` | 301 | 403 | 0.0274 | No | False | Safe / strict Host validation | Low |
| `tallnerk.ee` | `https` | 200 | 421 | 0.1276 | No | True | Safe / strict Host validation | Low |
| `tallnerk.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `basket.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `basket.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ilmateenistus.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ilmateenistus.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `hinnavaatlus.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `hinnavaatlus.ee` | `http` | 302 | 403 | 0.0342 | No | False | Safe / strict Host validation | Low |
| `parnu.ee` | `https` | 200 | 403 | 0.042 | No | False | Safe / strict Host validation | Low |
| `parnu.ee` | `http` | 301 | 403 | 0.035 | No | False | Safe / strict Host validation | Low |
| `sudameapteek.ee` | `https` | 301 | 301 | 0.928 | Location, Headers | True | Possible Host header injection | High |
| `sudameapteek.ee` | `http` | 301 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `juhanipuukool.ee` | `https` | 200 | 421 | 0.0072 | No | True | Safe / strict Host validation | Low |
| `juhanipuukool.ee` | `http` | 301 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `kelle-number.ee` | `https` | 301 | 421 | 0.3934 | No | True | Safe / strict Host validation | Low |
| `kelle-number.ee` | `http` | 301 | 403 | 0.014 | No | False | Safe / strict Host validation | Low |
| `mi-home.ee` | `https` | 200 | 403 | 0.035 | No | False | Safe / strict Host validation | Low |
| `mi-home.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `coin24.ee` | `https` | 200 | 403 | 0.0284 | No | False | Safe / strict Host validation | Low |
| `coin24.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `etis.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `etis.ee` | `http` | 302 | 403 | 0.0295 | No | False | Safe / strict Host validation | Low |
| `opiq.ee` | `https` | 307 | 404 | 0.0073 | No | False | Safe / strict Host validation | Low |
| `opiq.ee` | `http` | 307 | 403 | 0.0299 | No | False | Safe / strict Host validation | Low |
| `kava.ee` | `https` | 301 | 421 | 0.3995 | No | True | Safe / strict Host validation | Low |
| `kava.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `remit.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `remit.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `tophotel.ee` | `https` | 200 | 200 | 0.111 | No | False | Different content with same status | Low/Medium |
| `tophotel.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `trip.ee` | `https` | 200 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `trip.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `opleht.ee` | `https` | 301 | 302 | 0.0 | Location, Headers | False | Possible Host header injection | High |
| `opleht.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `moobliait.ee` | `https` | 200 | 403 | 0.02 | No | False | Safe / strict Host validation | Low |
| `moobliait.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `infoauto.ee` | `https` | 200 | 421 | 0.0085 | No | True | Safe / strict Host validation | Low |
| `infoauto.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `khk.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `khk.ee` | `http` | 301 | 403 | 0.0321 | No | False | Safe / strict Host validation | Low |
| `paf.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `paf.ee` | `http` | 403 | 403 | 0.3163 | No | False | Safe / strict Host validation | Low |
| `terviseportaal.ee` | `https` | 301 | 403 | 0.0101 | No | False | Safe / strict Host validation | Low |
| `terviseportaal.ee` | `http` | 302 | 403 | 0.0346 | No | False | Safe / strict Host validation | Low |
| `directo.ee` | `https` | 200 | 421 | 0.0104 | No | True | Safe / strict Host validation | Low |
| `directo.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `d0.ee` | `https` | 200 | 200 | 0.1393 | No | False | Different content with same status | Low/Medium |
| `d0.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `matkasport.ee` | `https` | 200 | 421 | 0.011 | No | True | Safe / strict Host validation | Low |
| `matkasport.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `mototehnika.ee` | `https` | 302 | 403 | 0.5227 | No | False | Safe / strict Host validation | Low |
| `mototehnika.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `k-space.ee` | `https` | 200 | 302 | 0.0658 | Location, Headers | True | Possible Host header injection | High |
| `k-space.ee` | `http` | 301 | 403 | 0.0037 | No | False | Safe / strict Host validation | Low |
| `playin.ee` | `https` | 301 | 403 | 0.7767 | No | False | Safe / strict Host validation | Low |
| `playin.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `apollokino.ee` | `https` | 301 | 403 | 0.1984 | No | False | Safe / strict Host validation | Low |
| `apollokino.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `folklore.ee` | `https` | 200 | 503 | 0.003 | No | False | Different response | Low |
| `folklore.ee` | `http` | 302 | 403 | 0.0129 | No | False | Safe / strict Host validation | Low |
| `almic.ee` | `https` | 200 | 200 | 0.021 | No | False | Different content with same status | Low/Medium |
| `almic.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `elering.ee` | `https` | 200 | 403 | 0.0329 | No | False | Safe / strict Host validation | Low |
| `elering.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `nsking.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `nsking.ee` | `http` | 403 | 403 | 0.0335 | No | False | Safe / strict Host validation | Low |
| `merit.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `merit.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `kul.ee` | `https` | 200 | 403 | 0.1724 | No | False | Safe / strict Host validation | Low |
| `kul.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `objektiiv.ee` | `https` | 200 | 421 | 0.0074 | No | True | Safe / strict Host validation | Low |
| `objektiiv.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `hansapost.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `hansapost.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `helmes.ee` | `https` | 301 | 301 | 0.9868 | No | False | Redirects invalid Host | Low/Medium |
| `helmes.ee` | `http` | 301 | 403 | 0.0351 | No | False | Safe / strict Host validation | Low |
| `luminor.ee` | `https` | 200 | 403 | 0.0385 | No | False | Safe / strict Host validation | Low |
| `luminor.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `hoathinh3d.ee` | `https` | 200 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `hoathinh3d.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `looduskalender.ee` | `https` | 301 | None | 0.0 | No | False | Inconclusive | Low |
| `looduskalender.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `br.ee` | `https` | 200 | 200 | 0.0 | No | False | Different content with same status | Low/Medium |
| `br.ee` | `http` | 308 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `tooriistamarket.ee` | `https` | 200 | 403 | 0.0217 | No | False | Safe / strict Host validation | Low |
| `tooriistamarket.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `olerex.ee` | `https` | 200 | 400 | 0.0162 | No | False | Safe / strict Host validation | Low |
| `olerex.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `lm.ee` | `https` | 200 | 404 | 0.0311 | No | False | Safe / strict Host validation | Low |
| `lm.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `masterlight.ee` | `https` | 200 | 403 | 0.0399 | No | False | Safe / strict Host validation | Low |
| `masterlight.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `tavid.ee` | `https` | 200 | 403 | 0.0154 | No | False | Safe / strict Host validation | Low |
| `tavid.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `yanhh3d.ee` | `https` | 200 | 403 | 0.03 | No | False | Safe / strict Host validation | Low |
| `yanhh3d.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `telset.ee` | `https` | 200 | 403 | 0.0272 | No | False | Safe / strict Host validation | Low |
| `telset.ee` | `http` | 301 | 403 | 0.0114 | No | False | Safe / strict Host validation | Low |
| `logo.ee` | `https` | 301 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `logo.ee` | `http` | 301 | 403 | 0.0153 | No | False | Safe / strict Host validation | Low |
| `eev.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `eev.ee` | `http` | 301 | 403 | 0.0311 | No | False | Safe / strict Host validation | Low |
| `bl.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `bl.ee` | `http` | 200 | 403 | 0.0244 | No | False | Safe / strict Host validation | Low |
| `bitflip.ee` | `https` | 200 | 421 | 0.0071 | No | True | Safe / strict Host validation | Low |
| `bitflip.ee` | `http` | 200 | 403 | 0.0453 | No | False | Safe / strict Host validation | Low |
| `omaraha.ee` | `https` | 302 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `omaraha.ee` | `http` | 301 | 403 | 0.0311 | No | False | Safe / strict Host validation | Low |
| `airport.ee` | `https` | 200 | 403 | 0.0334 | No | False | Safe / strict Host validation | Low |
| `airport.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `prismamarket.ee` | `https` | 308 | 404 | 0.0209 | No | False | Safe / strict Host validation | Low |
| `prismamarket.ee` | `http` | 308 | 403 | 0.0049 | No | False | Safe / strict Host validation | Low |
| `tlu.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `tlu.ee` | `http` | 302 | 403 | 0.0143 | No | False | Safe / strict Host validation | Low |
| `ergohiir.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `ergohiir.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `lounaeestlane.ee` | `https` | 200 | 421 | 0.009 | No | True | Safe / strict Host validation | Low |
| `lounaeestlane.ee` | `http` | 301 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `infoabi.ee` | `https` | 301 | 403 | 0.4058 | No | False | Safe / strict Host validation | Low |
| `infoabi.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `getapro.ee` | `https` | 200 | 404 | 0.0213 | No | False | Safe / strict Host validation | Low |
| `getapro.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `pepco.ee` | `https` | 200 | 403 | 0.0348 | No | False | Safe / strict Host validation | Low |
| `pepco.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `modernkids.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `modernkids.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `next.com.ee` | `https` | 301 | 400 | 0.0 | No | False | Safe / strict Host validation | Low |
| `next.com.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `paste.ee` | `https` | 200 | 500 | 0.0265 | No | False | Different response | Low |
| `paste.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `weekend.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `weekend.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `peatus.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `peatus.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ajapaik.ee` | `https` | 200 | 301 | 0.0273 | No | False | Redirects invalid Host | Low/Medium |
| `ajapaik.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `kinnisvara24.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `kinnisvara24.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `siseministeerium.ee` | `https` | None | 403 | 0.0 | No | False | Inconclusive | Unknown |
| `siseministeerium.ee` | `http` | 301 | 403 | 0.0105 | No | False | Safe / strict Host validation | Low |
| `polytrade.ee` | `https` | 200 | 421 | 0.0097 | No | True | Safe / strict Host validation | Low |
| `polytrade.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `perearst24.ee` | `https` | 301 | 404 | 1.0 | No | False | Safe / strict Host validation | Low |
| `perearst24.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `terminal.ee` | `https` | 200 | 421 | 0.0141 | No | True | Safe / strict Host validation | Low |
| `terminal.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `sm.ee` | `https` | 200 | 403 | 0.0311 | No | False | Safe / strict Host validation | Low |
| `sm.ee` | `http` | 301 | 403 | 0.0291 | No | False | Safe / strict Host validation | Low |
| `nulls.ee` | `https` | 302 | 200 | 0.0 | No | False | Different response | Low |
| `nulls.ee` | `http` | 301 | 403 | 0.033 | No | False | Safe / strict Host validation | Low |
| `hot.ee` | `https` | 302 | 404 | 0.4348 | No | False | Safe / strict Host validation | Low |
| `hot.ee` | `http` | 301 | 403 | 0.0025 | No | False | Safe / strict Host validation | Low |
| `autoparts.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `autoparts.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `decathlon.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `decathlon.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `kaitseministeerium.ee` | `https` | 200 | 403 | 0.0421 | No | False | Safe / strict Host validation | Low |
| `kaitseministeerium.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `itella.ee` | `https` | 301 | 302 | 0.0 | Location, Headers | False | Possible Host header injection | High |
| `itella.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `petcity.ee` | `https` | 301 | 301 | 0.9357 | Location, Headers | True | Possible Host header injection | High |
| `petcity.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `easysmoke.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `easysmoke.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `vm.ee` | `https` | 200 | 403 | 0.0293 | No | False | Safe / strict Host validation | Low |
| `vm.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `elektrihind.ee` | `https` | 200 | 403 | 0.0251 | No | False | Safe / strict Host validation | Low |
| `elektrihind.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `infoweb.ee` | `https` | 301 | 200 | 0.1478 | No | False | Different response | Low |
| `infoweb.ee` | `http` | 301 | 403 | 0.046 | No | False | Safe / strict Host validation | Low |
| `byroomaailm.ee` | `https` | 301 | 301 | 0.0 | No | False | Redirects invalid Host | Low/Medium |
| `byroomaailm.ee` | `http` | 301 | 403 | 0.0311 | No | False | Safe / strict Host validation | Low |
| `vanaraamat.ee` | `https` | 301 | 421 | 0.3902 | No | True | Safe / strict Host validation | Low |
| `vanaraamat.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `airbnb.com.ee` | `https` | 301 | 404 | 0.8219 | No | False | Safe / strict Host validation | Low |
| `airbnb.com.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `anextour.ee` | `https` | 200 | 404 | 0.0221 | No | False | Safe / strict Host validation | Low |
| `anextour.ee` | `http` | 308 | 403 | 0.0014 | No | False | Safe / strict Host validation | Low |
| `piletikeskus.ee` | `https` | 302 | 421 | 0.081 | No | True | Safe / strict Host validation | Low |
| `piletikeskus.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `animevietsub.ee` | `https` | 301 | 403 | 0.3491 | No | False | Safe / strict Host validation | Low |
| `animevietsub.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `physio.ee` | `https` | 403 | 402 | 0.1973 | Cookie, Headers | False | Possible Host header injection | High |
| `physio.ee` | `http` | 403 | 403 | 0.0402 | No | False | Safe / strict Host validation | Low |
| `paavlikaltsukas.ee` | `https` | 301 | 421 | 0.3878 | No | True | Safe / strict Host validation | Low |
| `paavlikaltsukas.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `frog.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `frog.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `hange.ee` | `https` | 301 | 404 | 0.0245 | No | False | Safe / strict Host validation | Low |
| `hange.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `vint.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `vint.ee` | `http` | 301 | 403 | 0.033 | No | False | Safe / strict Host validation | Low |
| `mke.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `mke.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `duoplay.ee` | `https` | 200 | 503 | 0.0197 | No | False | Different response | Low |
| `duoplay.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `osport.ee` | `https` | 200 | 404 | 0.0412 | No | False | Safe / strict Host validation | Low |
| `osport.ee` | `http` | 307 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `plussriided.ee` | `https` | 200 | 421 | 0.01 | No | True | Safe / strict Host validation | Low |
| `plussriided.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `ilm.ee` | `https` | 200 | 421 | 0.0107 | No | True | Safe / strict Host validation | Low |
| `ilm.ee` | `http` | 301 | 403 | 0.0132 | No | False | Safe / strict Host validation | Low |
| `taltech.ee` | `https` | 200 | 403 | 0.0308 | No | False | Safe / strict Host validation | Low |
| `taltech.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `starman.ee` | `https` | 302 | None | 1.0 | No | False | Inconclusive | Low |
| `starman.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `dv.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `dv.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `minijalgpall.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `minijalgpall.ee` | `http` | 301 | 403 | 0.023 | No | False | Safe / strict Host validation | Low |
| `elektrilevi.ee` | `https` | 200 | 403 | 0.0303 | No | False | Safe / strict Host validation | Low |
| `elektrilevi.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `puumarket.ee` | `https` | 200 | 421 | 0.008 | No | True | Safe / strict Host validation | Low |
| `puumarket.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `ristmik.ee` | `https` | 200 | 400 | 0.008 | No | False | Safe / strict Host validation | Low |
| `ristmik.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `online.ee` | `https` | 302 | 404 | 0.4348 | No | False | Safe / strict Host validation | Low |
| `online.ee` | `http` | 301 | 403 | 0.0025 | No | False | Safe / strict Host validation | Low |
| `hiiumaa.ee` | `https` | 200 | 421 | 0.0089 | No | True | Safe / strict Host validation | Low |
| `hiiumaa.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `jakarta.ee` | `https` | 200 | 404 | 0.0343 | No | False | Safe / strict Host validation | Low |
| `jakarta.ee` | `http` | 301 | 403 | 0.0097 | No | False | Safe / strict Host validation | Low |
| `transpordiamet.ee` | `https` | 200 | 403 | 0.0302 | No | False | Safe / strict Host validation | Low |
| `transpordiamet.ee` | `http` | 301 | 403 | 0.0274 | No | False | Safe / strict Host validation | Low |
| `kalkulaator.ee` | `https` | 301 | 421 | 0.3918 | No | True | Safe / strict Host validation | Low |
| `kalkulaator.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `glami.ee` | `https` | 301 | None | 0.0 | No | False | Inconclusive | Low |
| `glami.ee` | `http` | 301 | 403 | 0.0439 | No | False | Safe / strict Host validation | Low |
| `elamuteenused.ee` | `https` | 200 | 421 | 0.0083 | No | False | Safe / strict Host validation | Low |
| `elamuteenused.ee` | `http` | 200 | 403 | 0.0525 | No | False | Safe / strict Host validation | Low |
| `hotlips.ee` | `https` | 301 | 403 | 0.2525 | No | False | Safe / strict Host validation | Low |
| `hotlips.ee` | `http` | 301 | 403 | 0.0247 | No | False | Safe / strict Host validation | Low |
| `rit.ee` | `https` | 200 | 403 | 0.0333 | No | False | Safe / strict Host validation | Low |
| `rit.ee` | `http` | 301 | 403 | 0.0349 | No | False | Safe / strict Host validation | Low |
| `seb.ee` | `https` | 301 | 400 | 0.0 | No | False | Safe / strict Host validation | Low |
| `seb.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `yaga.ee` | `https` | 302 | 403 | 0.0334 | No | False | Safe / strict Host validation | Low |
| `yaga.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `qbe.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `qbe.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `iparts.ee` | `https` | 200 | 400 | 0.0112 | No | False | Safe / strict Host validation | Low |
| `iparts.ee` | `http` | 301 | 403 | 0.0139 | No | False | Safe / strict Host validation | Low |
| `enefit.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `enefit.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `atea.ee` | `https` | 301 | None | 1.0 | No | False | Inconclusive | Low |
| `atea.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `spacebear.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `spacebear.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `ralli.ee` | `https` | 200 | 421 | 0.007 | No | True | Safe / strict Host validation | Low |
| `ralli.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `kniga24.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `kniga24.ee` | `http` | 301 | 403 | 0.0123 | No | False | Safe / strict Host validation | Low |
| `ttu.ee` | `https` | 301 | 421 | 0.407 | No | True | Safe / strict Host validation | Low |
| `ttu.ee` | `http` | 301 | 403 | 0.0323 | No | False | Safe / strict Host validation | Low |
| `nscluster.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `nscluster.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `tv3.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `tv3.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `digikey.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `digikey.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `rune-server.ee` | `https` | 301 | 403 | 0.8543 | No | False | Safe / strict Host validation | Low |
| `rune-server.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `sisustusweb.ee` | `https` | 301 | 400 | 0.3355 | No | False | Safe / strict Host validation | Low |
| `sisustusweb.ee` | `http` | 301 | 403 | 0.0139 | No | False | Safe / strict Host validation | Low |
| `abakhan.ee` | `https` | 301 | 421 | 0.3959 | No | True | Safe / strict Host validation | Low |
| `abakhan.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `rasketehnika.ee` | `https` | 302 | 403 | 0.5212 | No | False | Safe / strict Host validation | Low |
| `rasketehnika.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `varuosakeskus.ee` | `https` | 200 | 421 | 0.0124 | No | False | Safe / strict Host validation | Low |
| `varuosakeskus.ee` | `http` | 301 | 403 | 0.0349 | No | False | Safe / strict Host validation | Low |
| `entsyklopeedia.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `entsyklopeedia.ee` | `http` | 200 | 403 | 0.0157 | No | False | Safe / strict Host validation | Low |
| `varuosamarket.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `varuosamarket.ee` | `http` | 301 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `riigiteataja.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `riigiteataja.ee` | `http` | 301 | 403 | 0.0274 | No | False | Safe / strict Host validation | Low |
| `lidl.ee` | `https` | 301 | 400 | 0.0 | No | False | Safe / strict Host validation | Low |
| `lidl.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `1182.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `1182.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `infopank.ee` | `https` | 301 | 403 | 0.3489 | No | False | Safe / strict Host validation | Low |
| `infopank.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `catnip.ee` | `https` | 200 | 200 | 0.0 | No | False | Different content with same status | Low/Medium |
| `catnip.ee` | `http` | 308 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `puhkaeestis.ee` | `https` | 307 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `puhkaeestis.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `reisidiilid.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `reisidiilid.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `cv.ee` | `https` | 307 | 403 | 0.0544 | No | False | Safe / strict Host validation | Low |
| `cv.ee` | `http` | 404 | 403 | 0.0025 | No | False | Safe / strict Host validation | Low |
| `hind.ee` | `https` | 301 | 403 | 0.447 | No | False | Safe / strict Host validation | Low |
| `hind.ee` | `http` | 301 | 403 | 0.0329 | No | False | Safe / strict Host validation | Low |
| `hhtq.ee` | `https` | 200 | 403 | 0.03 | No | False | Safe / strict Host validation | Low |
| `hhtq.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `kernel.ee` | `https` | 301 | 400 | 0.0 | No | False | Safe / strict Host validation | Low |
| `kernel.ee` | `http` | 301 | 403 | 0.0353 | No | False | Safe / strict Host validation | Low |
| `rostok.ee` | `https` | 200 | 302 | 0.0 | Location, Headers | False | Possible Host header injection | High |
| `rostok.ee` | `http` | 301 | 403 | 0.0434 | No | False | Safe / strict Host validation | Low |
| `flirtic.ee` | `https` | 301 | 200 | 0.0753 | No | False | Different response | Low |
| `flirtic.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `estravel.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `estravel.ee` | `http` | 302 | 403 | 0.0359 | No | False | Safe / strict Host validation | Low |
| `tai.ee` | `https` | 301 | 400 | 0.1136 | No | False | Safe / strict Host validation | Low |
| `tai.ee` | `http` | 301 | 403 | 0.0321 | No | False | Safe / strict Host validation | Low |
| `rug.ee` | `https` | 301 | 301 | 1.0 | Cookie, Headers | False | Possible Host header injection | High |
| `rug.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `tele2.ee` | `https` | 200 | 301 | 0.0309 | No | False | Redirects invalid Host | Low/Medium |
| `tele2.ee` | `http` | 301 | 403 | 0.0114 | No | False | Safe / strict Host validation | Low |
| `keeleklikk.ee` | `https` | 301 | 421 | 0.2811 | No | False | Safe / strict Host validation | Low |
| `keeleklikk.ee` | `http` | 302 | 403 | 0.036 | No | False | Safe / strict Host validation | Low |
| `sotsiaalkindlustusamet.ee` | `https` | 200 | 403 | 0.0254 | No | False | Safe / strict Host validation | Low |
| `sotsiaalkindlustusamet.ee` | `http` | 301 | 403 | 0.0265 | No | False | Safe / strict Host validation | Low |
| `ohtulehtkirjastus.ee` | `https` | 301 | 403 | 0.352 | No | False | Safe / strict Host validation | Low |
| `ohtulehtkirjastus.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `makeup.ee` | `https` | 200 | 403 | 0.0058 | No | False | Safe / strict Host validation | Low |
| `makeup.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `nommeraadio.ee` | `https` | 301 | 421 | 0.3887 | No | True | Safe / strict Host validation | Low |
| `nommeraadio.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `novayagazeta.ee` | `https` | 200 | 403 | 0.0237 | No | False | Safe / strict Host validation | Low |
| `novayagazeta.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `salmo.ee` | `https` | 302 | 302 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `salmo.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `surfhouse.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `surfhouse.ee` | `http` | 403 | 403 | 0.0328 | No | False | Safe / strict Host validation | Low |
| `aboutyou.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `aboutyou.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `korto.ee` | `https` | 200 | 200 | 0.998 | No | False | Weak Host validation | Medium |
| `korto.ee` | `http` | 302 | 403 | 0.0386 | No | False | Safe / strict Host validation | Low |
| `rce.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `rce.ee` | `http` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `jahipaun.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `jahipaun.ee` | `http` | 301 | 403 | 0.0318 | No | False | Safe / strict Host validation | Low |
| `synlab.ee` | `https` | 200 | 421 | 0.0097 | No | True | Safe / strict Host validation | Low |
| `synlab.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `kliinik.ee` | `https` | 301 | 200 | 0.0 | No | False | Different response | Low |
| `kliinik.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `bigbox.ee` | `https` | 200 | 403 | 0.0381 | No | False | Safe / strict Host validation | Low |
| `bigbox.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `sonumid.ee` | `https` | 200 | 403 | 0.0293 | No | False | Safe / strict Host validation | Low |
| `sonumid.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `esto.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `esto.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `srotas.ee` | `https` | 200 | 403 | 0.0375 | No | False | Safe / strict Host validation | Low |
| `srotas.ee` | `http` | 200 | 403 | 0.0736 | No | False | Safe / strict Host validation | Low |
| `decora.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `decora.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `lhv.ee` | `https` | 302 | 301 | 0.8879 | No | False | Redirects invalid Host | Low/Medium |
| `lhv.ee` | `http` | 301 | 403 | 0.0353 | No | False | Safe / strict Host validation | Low |
| `datagate.ee` | `https` | 200 | 500 | 0.0225 | No | False | Different response | Low |
| `datagate.ee` | `http` | 301 | 403 | 0.0109 | No | False | Safe / strict Host validation | Low |
| `astri.ee` | `https` | 302 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `astri.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `salva.ee` | `https` | 301 | 434 | 0.0 | No | False | Different response | Low |
| `salva.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `confido.ee` | `https` | 301 | 421 | 0.0 | No | True | Safe / strict Host validation | Low |
| `confido.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `sumena.ee` | `https` | 200 | 421 | 0.0085 | No | True | Safe / strict Host validation | Low |
| `sumena.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `bauhub.ee` | `https` | 200 | 301 | 0.0381 | Location, Headers | False | Possible Host header injection | High |
| `bauhub.ee` | `http` | 301 | 403 | 0.0296 | No | False | Safe / strict Host validation | Low |
| `01.ee` | `https` | 308 | 403 | 0.1921 | No | False | Safe / strict Host validation | Low |
| `01.ee` | `http` | 308 | 403 | 0.0121 | No | False | Safe / strict Host validation | Low |
| `edel-infra.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `edel-infra.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `inforegister.ee` | `https` | 301 | 200 | 0.0 | No | False | Different response | Low |
| `inforegister.ee` | `http` | 301 | 403 | 0.035 | No | False | Safe / strict Host validation | Low |
| `visittallinn.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `visittallinn.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `staycool.ee` | `https` | 301 | 503 | 0.0 | No | False | Different response | Low |
| `staycool.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `praamid.ee` | `https` | 302 | 403 | 0.253 | No | False | Safe / strict Host validation | Low |
| `praamid.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `kovtp.ee` | `https` | 302 | 200 | 0.0627 | No | False | Different response | Low |
| `kovtp.ee` | `http` | 302 | 403 | 0.014 | No | False | Safe / strict Host validation | Low |
| `co.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `co.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `tdk.ee` | `https` | 200 | 301 | 0.0406 | Location, Headers | False | Possible Host header injection | High |
| `tdk.ee` | `http` | 301 | 403 | 0.0065 | No | False | Safe / strict Host validation | Low |
| `koda.ee` | `https` | 301 | 421 | 0.3726 | No | False | Safe / strict Host validation | Low |
| `koda.ee` | `http` | 301 | 403 | 0.0356 | No | False | Safe / strict Host validation | Low |
| `nss.ee` | `https` | 302 | 200 | 0.1807 | No | False | Different response | Low |
| `nss.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `radicenter.ee` | `https` | 301 | 421 | 0.5145 | No | True | Safe / strict Host validation | Low |
| `radicenter.ee` | `http` | 301 | 403 | 0.0153 | No | False | Safe / strict Host validation | Low |
| `kriso.ee` | `https` | 301 | 403 | 0.4946 | No | False | Safe / strict Host validation | Low |
| `kriso.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `automoto.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `automoto.ee` | `http` | 200 | 403 | 0.0166 | No | False | Safe / strict Host validation | Low |
| `kl24.ee` | `https` | 200 | 200 | 1.0 | No | False | Weak Host validation | Medium |
| `kl24.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `lambimaailm.ee` | `https` | 301 | 301 | 1.0 | Location, Headers | False | Possible Host header injection | High |
| `lambimaailm.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `novatours.ee` | `https` | 301 | 403 | 0.3456 | No | False | Safe / strict Host validation | Low |
| `novatours.ee` | `http` | 301 | 403 | 0.0237 | No | False | Safe / strict Host validation | Low |
| `terviserajad.ee` | `https` | 200 | 421 | 0.0071 | No | False | Safe / strict Host validation | Low |
| `terviserajad.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `estnoc.ee` | `https` | 301 | 421 | 0.372 | No | False | Safe / strict Host validation | Low |
| `estnoc.ee` | `http` | 404 | 403 | 0.0153 | No | False | Safe / strict Host validation | Low |
| `politsei.ee` | `https` | 301 | 403 | 0.3489 | No | False | Safe / strict Host validation | Low |
| `politsei.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `super.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `super.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `kanal2.ee` | `https` | 302 | 503 | 0.235 | No | False | Different response | Low |
| `kanal2.ee` | `http` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `adm.ee` | `https` | 301 | 421 | 0.0 | No | False | Safe / strict Host validation | Low |
| `adm.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `feb.ee` | `https` | 301 | 500 | 0.0 | No | False | Different response | Low |
| `feb.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `allcar.ee` | `https` | 200 | 421 | 0.0148 | No | True | Safe / strict Host validation | Low |
| `allcar.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `kodumasin.ee` | `https` | 200 | 421 | 0.0131 | No | True | Safe / strict Host validation | Low |
| `kodumasin.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `tervisetrend.ee` | `https` | 200 | 421 | 0.0102 | No | True | Safe / strict Host validation | Low |
| `tervisetrend.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `juristaitab.ee` | `https` | 302 | 403 | 0.2653 | No | False | Safe / strict Host validation | Low |
| `juristaitab.ee` | `http` | 301 | 403 | 0.0117 | No | False | Safe / strict Host validation | Low |
| `soudeliit.ee` | `https` | 301 | 403 | 0.4148 | No | False | Safe / strict Host validation | Low |
| `soudeliit.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `blogspot.com.ee` | `https` | 404 | 404 | 1.0 | No | False | Safe / strict Host validation | Low |
| `blogspot.com.ee` | `http` | 404 | 403 | 0.0841 | No | False | Safe / strict Host validation | Low |
| `proxy.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `proxy.ee` | `http` | 200 | 403 | 0.0113 | No | False | Safe / strict Host validation | Low |
| `photopoint.ee` | `https` | 301 | 200 | 0.0093 | No | False | Different response | Low |
| `photopoint.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `bodyvision.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `bodyvision.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `fin.ee` | `https` | 200 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `fin.ee` | `http` | 301 | 403 | 0.0116 | No | False | Safe / strict Host validation | Low |
| `inlink.ee` | `https` | 200 | 403 | 0.0715 | No | False | Safe / strict Host validation | Low |
| `inlink.ee` | `http` | 307 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `textm.ee` | `https` | 200 | 403 | 0.0573 | No | False | Safe / strict Host validation | Low |
| `textm.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `opbank.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `opbank.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `harno.ee` | `https` | 200 | 403 | 0.0306 | No | False | Safe / strict Host validation | Low |
| `harno.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `otp.ee` | `https` | 429 | 403 | 0.0504 | No | False | Safe / strict Host validation | Low |
| `otp.ee` | `http` | 429 | 403 | 0.0229 | No | False | Safe / strict Host validation | Low |
| `aso.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `aso.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `vidaxl.ee` | `https` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `vidaxl.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `bondora.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `bondora.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `velomarket.ee` | `https` | 200 | 403 | 0.1169 | No | False | Safe / strict Host validation | Low |
| `velomarket.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `ox.ee` | `https` | 308 | 403 | 0.1576 | No | False | Safe / strict Host validation | Low |
| `ox.ee` | `http` | 308 | 403 | 0.0171 | No | False | Safe / strict Host validation | Low |
| `topauto.ee` | `https` | 301 | 200 | 0.0 | No | False | Different response | Low |
| `topauto.ee` | `http` | 301 | 403 | 0.0456 | No | False | Safe / strict Host validation | Low |
| `novartis.ee` | `https` | 301 | 403 | 0.352 | No | False | Safe / strict Host validation | Low |
| `novartis.ee` | `http` | 301 | 403 | 0.0137 | No | False | Safe / strict Host validation | Low |
| `smit.ee` | `https` | 301 | 301 | 1.0 | No | False | Redirects invalid Host | Low/Medium |
| `smit.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `betsafe.ee` | `https` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `betsafe.ee` | `http` | 403 | 403 | 1.0 | No | False | Safe / strict Host validation | Low |
| `moto24.ee` | `https` | 200 | 403 | 0.0288 | No | False | Safe / strict Host validation | Low |
| `moto24.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `just.ee` | `https` | 301 | 403 | 0.2634 | No | False | Safe / strict Host validation | Low |
| `just.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `teibid.ee` | `https` | 301 | 200 | 0.0 | Body | False | Possible Host header injection | Medium |
| `teibid.ee` | `http` | 301 | 403 | 0.0319 | No | False | Safe / strict Host validation | Low |
| `aki.ee` | `https` | 302 | 403 | 0.268 | No | False | Safe / strict Host validation | Low |
| `aki.ee` | `http` | 301 | 403 | 0.0349 | No | False | Safe / strict Host validation | Low |
| `diveevo-shop.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `diveevo-shop.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `tuuliretseptid.ee` | `https` | 200 | 421 | 0.0097 | No | True | Safe / strict Host validation | Low |
| `tuuliretseptid.ee` | `http` | 301 | 403 | 0.0315 | No | False | Safe / strict Host validation | Low |
| `x3000.ee` | `https` | 301 | 403 | 0.352 | No | False | Safe / strict Host validation | Low |
| `x3000.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `veli.ee` | `https` | 200 | 421 | 0.0091 | No | False | Safe / strict Host validation | Low |
| `veli.ee` | `http` | 302 | 403 | 0.0313 | No | False | Safe / strict Host validation | Low |
| `zalando.ee` | `https` | 302 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `zalando.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `go3.ee` | `https` | 403 | 403 | 0.0336 | No | False | Safe / strict Host validation | Low |
| `go3.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `euroapteek.ee` | `https` | 301 | 403 | 0.352 | No | False | Safe / strict Host validation | Low |
| `euroapteek.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `lakinet.ee` | `https` | 200 | 200 | 0.0218 | No | False | Different content with same status | Low/Medium |
| `lakinet.ee` | `http` | 301 | 403 | 0.0316 | No | False | Safe / strict Host validation | Low |
| `starmoto.ee` | `https` | 403 | 403 | 0.0432 | No | False | Safe / strict Host validation | Low |
| `starmoto.ee` | `http` | 301 | 403 | 0.0231 | No | False | Safe / strict Host validation | Low |
| `rehviliider.ee` | `https` | 301 | 200 | 1.0 | No | False | Different response | Low |
| `rehviliider.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `tuusik.ee` | `https` | 301 | 421 | 0.0761 | No | True | Safe / strict Host validation | Low |
| `tuusik.ee` | `http` | 301 | 403 | 0.0131 | No | False | Safe / strict Host validation | Low |
| `www.ee` | `https` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `www.ee` | `http` | None | None | 1.0 | No | False | Inconclusive | Unknown |
| `youtube.com.ee` | `https` | 301 | 404 | 0.0 | No | False | Safe / strict Host validation | Low |
| `youtube.com.ee` | `http` | 301 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `city24.ee` | `https` | 301 | 403 | 0.8013 | No | False | Safe / strict Host validation | Low |
| `city24.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `inbank.ee` | `https` | 200 | 403 | 0.0152 | No | False | Safe / strict Host validation | Low |
| `inbank.ee` | `http` | 301 | 403 | 0.0314 | No | False | Safe / strict Host validation | Low |
| `itk.ee` | `https` | 301 | 400 | 0.125 | No | False | Safe / strict Host validation | Low |
| `itk.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |
| `alvadi.ee` | `https` | 403 | 403 | 0.0503 | No | False | Safe / strict Host validation | Low |
| `alvadi.ee` | `http` | 301 | 403 | 0.01 | No | False | Safe / strict Host validation | Low |
| `veloplus.ee` | `https` | 302 | 301 | 0.3587 | No | False | Redirects invalid Host | Low/Medium |
| `veloplus.ee` | `http` | 301 | 403 | 0.0114 | No | False | Safe / strict Host validation | Low |
| `euautoosad.ee` | `https` | 403 | 403 | 0.034 | No | False | Safe / strict Host validation | Low |
| `euautoosad.ee` | `http` | 308 | 403 | 0.0 | No | False | Safe / strict Host validation | Low |
| `valgekihv.ee` | `https` | 200 | 421 | 0.0091 | No | True | Safe / strict Host validation | Low |
| `valgekihv.ee` | `http` | 301 | 403 | 0.0317 | No | False | Safe / strict Host validation | Low |
| `eelk.ee` | `https` | 200 | 421 | 0.0116 | No | True | Safe / strict Host validation | Low |
| `eelk.ee` | `http` | 301 | 403 | 0.032 | No | False | Safe / strict Host validation | Low |