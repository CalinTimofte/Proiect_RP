; (load "C:\\Users\\Pintilii\\Downloads\\PBR_LAB\\Proiect.clp")

(deffacts Facts
;	(MaP)
;	(SaM)
;	(SaP)
;	(Running)
)

(defrule X
	(Running)
	=>
	(printout t "Nu exista rezultat!")
	(printout t crlf)
)

(defrule A
	?x <- (Running)
	(not (exists (Finish)) )
	(concluzia SaP)
	(or
		(and (premisa1 MaP) (premisa2 SaM) )
		(and (premisa1 SaM) (premisa2 MaP) )
	)
	=>
	(printout t "Rezultat corect, SaP!" crlf)
	(assert (Finish))
	(retract ?x)
)

(defrule E
	?x <- (Running)
	(not (exists (Finish)) )
	(concluzia SeP)
	(or
		(and (premisa1 PaM) (premisa2 SeM) )
		(and (premisa1 SeM) (premisa2 PaM) )
		(and (premisa1 PaM) (premisa2 MeS) )
		(and (premisa1 MeS) (premisa2 PaM) )
		(and (premisa1 MeP) (premisa2 SaM) )
		(and (premisa1 SaM) (premisa2 MeP) )
		(and (premisa1 PeM) (premisa2 SaM) )
		(and (premisa1 SaM) (premisa2 PeM) )
	)
	=>
	(printout t "Rezultat corect, SeP!" crlf)
	(assert (Finish))
	(retract ?x)
)

(defrule I
	?x <- (Running)
	(not (exists (Finish)) )
	(concluzia SiP)
	(or
		(and (premisa1 MaP) (premisa2 SiM) )
		(and (premisa1 SiM) (premisa2 MaP) )
		(and (premisa1 MaP) (premisa2 MiS) )
		(and (premisa1 MiS) (premisa2 MaP) )
		(and (premisa1 MiP) (premisa2 MaS) )
		(and (premisa1 MaS) (premisa2 MiP) )
		(and (premisa1 PiM) (premisa2 MaS) )
		(and (premisa1 MaS) (premisa2 PiM) )
	)
	=>
	(printout t "Rezultat corect, SiP!" crlf)
	(assert (Finish))
	(retract ?x)
)

(defrule O
	?x <- (Running)
	(not (exists (Finish)) )
	(concluzia SoP)
	(or
		(and (premisa1 PaM) (premisa2 SoM) )
		(and (premisa1 SoM) (premisa2 PaM) )
		(and (premisa1 MoP) (premisa2 MaS) )
		(and (premisa1 MaS) (premisa2 MoP) )
		(and (premisa1 MeP) (premisa2 SiM) )
		(and (premisa1 SiM) (premisa2 MeP) )
		(and (premisa1 PeM) (premisa2 SiM) )
		(and (premisa1 SiM) (premisa2 PeM) )
		(and (premisa1 MeP) (premisa2 MiS) )
		(and (premisa1 MiS) (premisa2 MeP) )
		(and (premisa1 PeM) (premisa2 MiS) )
		(and (premisa1 MiS) (premisa2 PeM) )
	)
	=>
	(printout t "Rezultat corect, SoP!" crlf)
	(assert (Finish))
	(retract ?x)
)