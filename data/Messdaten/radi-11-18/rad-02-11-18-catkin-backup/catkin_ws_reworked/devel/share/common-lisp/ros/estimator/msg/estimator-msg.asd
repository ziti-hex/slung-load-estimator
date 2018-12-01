
(cl:in-package :asdf)

(defsystem "estimator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "cam" :depends-on ("_package_cam"))
    (:file "_package_cam" :depends-on ("_package"))
  ))