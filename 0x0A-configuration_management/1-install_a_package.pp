# Ensures the gem linter is installed
package { 'puppet-lint' :
ensure   => installed,
provider => 'gem',
}
