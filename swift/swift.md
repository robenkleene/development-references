# Swift

## Observers

`removeObserver` no longer needs to be called.

[OS X El Capitan v10.11](https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_11.html#//apple_ref/doc/uid/TP40016227-SW1): 

> NSNotificationCenter and NSDistributedNotificationCenter no longer send notifications to registered observers that may be deallocated. If the observer is able to be stored as a zeroing-weak reference the underlying storage stores the observer as a zeroing weak reference. Alternatively, if the object cannot be stored weakly (because it has a custom retain/release mechanism that would prevent the runtime from being able to store the object weakly) the object is stored as a non-weak zeroing reference. This means that observers are not required to un-register in their deallocation method.
