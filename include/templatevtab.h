


#ifndef _CTEMPLATEVTAB_H
#define _CTEMPLATEVTAB_H

#include "sqlite3.h"

#ifdef __cplusplus
extern "C" {
#endif

int sqlite3_templatevtab_init(sqlite3*, char**, const sqlite3_api_routines*);

#ifdef __cplusplus
}  /* end of the 'extern "C"' block */
#endif

#endif /* ifndef _TEMPLATEVTAB_H */
  