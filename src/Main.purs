module Main where

import Effect
import NumPy
import Prelude
import Tutorials.Core
import Effect.Class.Console (logShow)

test :: S (S Z) :+: S Z
test = auto

n1 :: S Z
n1 = auto

n2 = eval (n1 :+: n1)

main :: Effect Unit
main = do
  logShow $ asInt $ eval test
  let x = init (eval $ n2 :+: n2) (eval $ n2 :+: n1) 6
  logShow x
  let y = init (eval $ n1 :+: n2) (eval $ n2 :+: n2) 6
  logShow $ x `matmul` y