'''
Created on Oct 16, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GL.exceptional import glDeleteTextures
from Image import open

textureLoaderTextures = {}
    
def loadTexture (filename):
    
    global textureLoaderTextures
    
    # if texture already loaded return its id
    if filename in textureLoaderTextures:
        return textureLoaderTextures[filename]
    
    # load image
    image = open(filename)
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)
    
    # Create Texture
    textureId = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textureId)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    # save and return texture id
    textureLoaderTextures[filename] = textureId
    return textureId

def loadSphereTexture (filename):
    
    global textureLoaderTextures
    
    # if texture already loaded return its id
    if filename in textureLoaderTextures:
        return textureLoaderTextures[filename]
    
    # load image
    image = open(filename)
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)
    
    # Create Texture
    textureId = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textureId)
    
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    # save and return texture id
    textureLoaderTextures[filename] = textureId
    return textureId

def destroyTexture (textureId = None):
    
    global textureLoaderTextures
    
    if textureId == None:
        for textureFile in textureLoaderTextures:
            destroyTexture.destroy(textureLoaderTextures[textureFile])
    else:
        glDeleteTextures(1,[textureId])

