class zulip_ops::postgres_master {
  include zulip_ops::base
  include zulip_ops::postgres_appdb

  $master_packages = [# Packages needed for disk + RAID configuration
                      "xfsprogs",
                      "mdadm",
                      ]
  package { $master_packages: ensure => "installed" }

  file { '/etc/sysctl.d/40-postgresql.conf':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => 644,
    source   => 'puppet:///modules/zulip_ops/postgresql/40-postgresql.conf.master',
  }

  file { "/etc/postgresql/9.1/main/postgresql.conf":
    require => Package["postgresql-9.1"],
    ensure => file,
    owner  => "postgres",
    group  => "postgres",
    mode => 644,
    source => "puppet:///modules/zulip_ops/postgresql/postgresql.conf.master",
  }

  file { "/root/setup_disks.sh":
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => 744,
    source => 'puppet:///modules/zulip_ops/postgresql/setup_disks.sh',
  }

  exec { "setup_disks":
    command => "/root/setup_disks.sh",
    require => Package["postgresql-9.1", "xfsprogs", "mdadm"],
    creates => "/dev/md0"
  }
}
