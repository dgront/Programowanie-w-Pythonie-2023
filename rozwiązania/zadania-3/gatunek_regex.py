import re

regex = "\[.*\]"

text = """
>> KAH7860570.1  hypothetical protein Vadar_014987 [Vaccinium darrowii]
   #    score  bias  c-Evalue  i-Evalue hmmfrom  hmm to    alifrom  ali to    envfrom  env to     acc
 ---   ------ ----- --------- --------- ------- -------    ------- -------    ------- -------    ----
   1 !   64.0   0.1   5.9e-17   3.6e-13     222     396 ..     273     461 ..     246     493 .. 0.81

>> RZS12181.1  hypothetical protein BHM03_00043603 [Ensete ventricosum]
   #    score  bias  c-Evalue  i-Evalue hmmfrom  hmm to    alifrom  ali to    envfrom  env to     acc
 ---   ------ ----- --------- --------- ------- -------    ------- -------    ------- -------    ----
   1 !   64.1   0.1   5.6e-17   3.4e-13     247     402 ..     304     476 ..     136     494 .. 0.74

>> PIA58214.1  hypothetical protein AQUCO_00500270v1 [Aquilegia coerulea]
   #    score  bias  c-Evalue  i-Evalue hmmfrom  hmm to    alifrom  ali to    envfrom  env to     acc
 ---   ------ ----- --------- --------- ------- -------    ------- -------    ------- -------    ----
   1 !   65.1   0.0   2.7e-17   1.7e-13     215     395 ..     264     463 ..     190     490 .. 0.77

>> XP_042592971.1  steroid 17-alpha-hydroxylase/17,20 lyase isoform X1 [Cyprinus carpio]
   #    score  bias  c-Evalue  i-Evalue hmmfrom  hmm to    alifrom  ali to    envfrom  env to     acc
 ---   ------ ----- --------- --------- ------- -------    ------- -------    ------- -------    ----
   1 !   65.0   0.0   2.9e-17   1.7e-13     251     423 ..     308     499 ..     146     508 .. 0.81"""

for line in text.split("\n"):
    out = re.findall(regex, line)
    if len(out) > 0:
        print(out)