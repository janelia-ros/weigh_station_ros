;; This file is generated automatically from .metadata.org
;; File edits may be overwritten!
(require 'org)

(eval-after-load "org"
  '(require 'ox-gfm nil t))

(setq make-backup-files nil)
(setq org-confirm-babel-evaluate nil)

(org-babel-do-load-languages
 'org-babel-load-languages
 '((emacs-lisp . t)
   (lisp . t)
   (shell . t)
   (scheme . t)))

(defun tangle-org (org-file)
  "Tangle org file"
  (unless (string= "org" (file-name-extension org-file))
    (error "INFILE must be an org file."))
  (org-babel-tangle-file org-file))

(defun export-org (org-file)
  "Export org file to gfm file"
  (unless (string= "org" (file-name-extension org-file))
    (error "INFILE must be an org file."))
  (let ((org-file-buffer (find-file-noselect org-file)))
    (with-current-buffer org-file-buffer
      (org-open-file (org-gfm-export-to-markdown)))))

(defun process-org (org-file)
  "Tangle and export org file"
  (progn (tangle-org org-file)
         (export-org org-file)))

(make-variable-buffer-local 'org-export-filter-final-output-functions)
(defun my-double-blank-line-filter (output backend info)
  (replace-regexp-in-string "^\n+" "\n" output))
(add-to-list 'org-export-filter-final-output-functions
             'my-double-blank-line-filter)
(defun my-result-keyword-filter (output backend info)
  (replace-regexp-in-string "^#[+]RESULTS:.*\n" "" output))
(add-to-list 'org-export-filter-final-output-functions
             'my-result-keyword-filter)
(defun my-export-filename-filter (output backend info)
  (replace-regexp-in-string "^#[+]EXPORT_FILE_NAME:.*\n" "" output))
(add-to-list 'org-export-filter-final-output-functions
             'my-export-filename-filter)
