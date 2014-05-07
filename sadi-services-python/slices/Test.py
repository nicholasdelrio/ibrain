'''
Created on May 6, 2014

@author: nick

'''
#Simple program for ITK image read/write in Python

import itk
import itkTypes

pixelType = itkTypes.UC
imageType = itk.Image[pixelType, 2]
readerType = itk.ImageFileReader[imageType]
writerType = itk.ImageFileWriter[imageType]

reader = readerType.New()
writer = writerType.New()
reader.SetFileName( '/home/nick/Downloads/car.jpg' )
writer.SetFileName( '/home/nick/Downloads/car2.jpg' )
writer.SetInput( reader.GetOutput() )
writer.Update()