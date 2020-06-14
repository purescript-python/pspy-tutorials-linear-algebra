module Tutorials.Core(
    Refl(..),
    class IsSin,
    class Eval,
    class LE,
    class IsNat,
    sym,
    reduce,
    eval,
    Z(..),
    S(..),
    T(..),
    F(..),
    Plus(..),
    Mul(..),
    auto,
    asInt,
    plusNonZero,
    plusZero,
    mulNonZero,
    mulZero,
    (:+:),
    (:=:),
    (:*:),
    type (:+:),
    type (:=:),
    type (:*:)
) where

import Prelude

class IsSin a where
  auto :: a

infixl 2 type Refl as :=:
infixl 2 Refl as :=:
data Refl a b = Refl a b
instance reflIsSin :: (IsSin a, IsSin b) => IsSin (a :=: b) where auto = auto :=: auto
derive instance eqRefl :: (Eq a, Eq b) => Eq (Refl a b)

sym :: forall a b. IsSin a => IsSin b => Refl a b -> Refl b a
sym (a :=: b) = b :=: a

reduce :: forall a b. IsSin a => IsSin b => a :=: b -> a -> b
reduce _ _ = auto

class IsNat a where
  asInt :: a -> Int

data Z = Z
instance zIsS :: IsSin Z where auto = Z
instance zIsNat :: IsNat Z where asInt _ = 0
derive instance eqZ :: Eq Z

data S n = S n
instance sNIsS :: IsSin n => IsSin(S n) where auto = S auto
instance isNatReduction :: IsNat a => IsNat (S a) where asInt (S x) = 1 + asInt x
derive instance eqS :: Eq n => Eq (S n)

data T = T
instance tIsS :: IsSin T where auto = T
derive instance eqT :: Eq T

data F = F
instance fIsS :: IsSin F where auto = F
derive instance eqF :: Eq F


infixl 5 type Plus as :+:
infixl 5 Plus as :+:
data Plus a b = Plus a b
instance plusIsS :: (IsSin a, IsSin b) => IsSin (a :+: b) where auto = auto :+: auto


plusZero :: forall a. IsSin a => a :+: Z :=: a
plusZero = auto

plusNonZero :: forall a b. IsSin a => IsSin b => a :+: S b :=: S a :+: b
plusNonZero = auto

infixl 6 type Mul as :*:
infixl 6 Mul as :*:
data Mul a b = Mul a b
instance mulIsS :: (IsSin a, IsSin b) => IsSin (Mul a b) where auto = Mul auto auto

mulZero :: forall a. IsSin a => a :*: Z :=: Z
mulZero = auto

mulNonZero :: forall a b. IsSin a => IsSin b => (a :*: S b) :=: (a :*: b :+: a)
mulNonZero = auto

class Eval term value | term -> value

instance e1 :: Eval Z Z
instance e2 :: Eval n m => Eval (S n) (S m)
instance e3 :: Eval a a' => Eval (a :+: Z) a
instance e4 :: (Eval a a',  Eval b b', Eval (a :+: b) c) => Eval (a :+: S b) (S c)

class (IsNat val1, IsNat val2) <= LE val1 val2

instance le1 :: IsNat a => LE Z a
instance le2 :: LE a b => LE (S a) (S b)


eval :: forall term value. IsSin value => Eval term value => term -> value
eval _ = auto