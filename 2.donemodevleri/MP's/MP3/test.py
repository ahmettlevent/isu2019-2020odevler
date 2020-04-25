def readfile(filename):
  lines=[line for line in open(filename, "r").readlines()]
  rownames=[]
  data=[]
  for line in lines:
    p=line.strip().split(',')
    # First column in each row is the rowname
    rownames.append(p[0])
    # The data for this row is the remainder of the row
    data.append([x for x in p[1:]])
  dataDict = dict(zip(rownames, data))
  return dataDict
