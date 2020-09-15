(declare-const x Bool)
(declare-const y Bool)
(declare-const z Bool)

(declare-fun phi (Bool Bool Bool) Bool)
(assert
    (= 
        (phi x y z)
        (or 
            (and x y)
            (and y z)
            (and x z)
        )
    )
)

(declare-fun psi (Bool Bool Bool) Bool)
(assert
    (= 
        (psi x y z)
        (and 
            (or x y)
            (or y z)
            (or x z)
        )
    )
)

(assert
    (=
        (phi x y z)
        (psi x y z)
    )
)

(check-sat)

(assert
    (not
        (=
            (phi x y z)
            (psi x y z)
        )
    )
)

(check-sat)