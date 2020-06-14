unsafeCompareImpl = lambda lt: lambda eq: lambda gt: lambda x: lambda y: (
    lt if x < y else
    eq if x == y else
    gt
)
