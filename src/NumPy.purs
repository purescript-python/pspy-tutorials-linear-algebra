module NumPy where

import Data.Symbol
import Prelude
import Tutorials.Core

data Matrix m n a

class PyInferType a (s :: Symbol) | a -> s
instance inferInt :: PyInferType Int "i4"
else
instance inferNum :: PyInferType Number "f8"
else
instance inferBool :: PyInferType Boolean "?"
else
instance inferOther :: PyInferType a "O"


getTypeString :: forall a s. IsSymbol s => PyInferType a s => String
getTypeString = reflectSymbol (SProxy :: SProxy s)



foreign import unsafeCoerce :: forall a b. a -> b

foreign import concat :: forall m n1 n2 n3 a.
    Eval (n1 :+: n2) n3 => Matrix m n1 a -> Matrix m n2 a -> Matrix m n3 a

foreign import _index :: forall m n a. Int -> Int -> Matrix m n a -> a

index ::  forall m n i j a. LE i m => LE j n => i -> j -> Matrix m n a -> a
index a b x = _index (asInt a) (asInt b) x

foreign import matmul :: forall m n k a.
    Matrix m n a -> Matrix n k a -> Matrix m k a

foreign import _init :: forall m n a. Int -> Int -> String -> a -> Matrix m n a

init :: forall m n s a. IsNat m => IsNat n => IsSymbol s => PyInferType a s =>
        m -> n -> a -> Matrix m n a
init m n a = _init (asInt m) (asInt n) (reflectSymbol (SProxy :: SProxy s)) a

foreign import show_mat :: forall m n a. Matrix m n a -> String

instance ___ :: Show (Matrix m n a) where
    show = show_mat
